import random
import time


# --------------------------------------------------
# Local Search with Random Restart
# --------------------------------------------------
def solve_nqueens_ls(n, max_restarts=500, max_steps=2000):
    for restart in range(max_restarts):

        # random initial solution
        Q = [random.randrange(n) for _ in range(n)]

        # counters (Lecture 7)
        col = [0] * n
        diag1 = [0] * (2 * n)
        diag2 = [0] * (2 * n)

        for i in range(n):
            col[Q[i]] += 1
            diag1[i + Q[i]] += 1
            diag2[i - Q[i] + n] += 1

        def conflicts(i):
            return (
                col[Q[i]] +
                diag1[i + Q[i]] +
                diag2[i - Q[i] + n] - 3
            )

        for step in range(max_steps):

            # total conflicts
            total = sum(conflicts(i) for i in range(n))
            if total == 0:
                return Q, restart, step

            # select most conflicting queens
            max_c = max(conflicts(i) for i in range(n))
            rows = [i for i in range(n) if conflicts(i) == max_c]
            r = random.choice(rows)

            best_col = Q[r]
            best_conf = conflicts(r)

            # try all columns
            for c in range(n):
                if c == Q[r]:
                    continue

                # remove
                col[Q[r]] -= 1
                diag1[r + Q[r]] -= 1
                diag2[r - Q[r] + n] -= 1

                # try new
                col[c] += 1
                diag1[r + c] += 1
                diag2[r - c + n] += 1

                new_conf = (
                    col[c] +
                    diag1[r + c] +
                    diag2[r - c + n] - 3
                )

                # restore
                col[c] -= 1
                diag1[r + c] -= 1
                diag2[r - c + n] -= 1

                col[Q[r]] += 1
                diag1[r + Q[r]] += 1
                diag2[r - Q[r] + n] += 1

                if new_conf < best_conf or (
                    new_conf == best_conf and random.random() < 0.3
                ):
                    best_conf = new_conf
                    best_col = c


            # apply best move
            col[Q[r]] -= 1
            diag1[r + Q[r]] -= 1
            diag2[r - Q[r] + n] -= 1

            Q[r] = best_col

            col[Q[r]] += 1
            diag1[r + Q[r]] += 1
            diag2[r - Q[r] + n] += 1

    return None, None, None


# --------------------------------------------------
# MAIN
# --------------------------------------------------
if __name__ == "__main__":
    Ns = [8, 10, 12, 15, 20, 30, 40, 50, 100]

    with open("results.txt", "w") as f:
        for n in Ns:
            print(f"Solving {n}-Queens (Local Search)...")
            start = time.time()

            solution, restarts, steps = solve_nqueens_ls(n)

            elapsed = time.time() - start

            f.write(f"N = {n}\n")
            if solution is None:
                f.write("No solution found\n\n")
            else:
                f.write(f"Restarts = {restarts}\n")
                f.write(f"Steps = {steps}\n")
                f.write(f"Time = {elapsed:.4f} s\n")
                f.write(f"Solution = {solution}\n\n")

    print("Done. Results saved in results.txt")
