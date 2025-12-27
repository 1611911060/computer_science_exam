from amplify import VariableGenerator, FixstarsClient, Model, solve
import time

# --------------------------------------------------
# N values to test
# --------------------------------------------------
Ns = [8, 10, 12, 15, 20, 30, 40, 50, 100]


# --------------------------------------------------
# Solve N-Queens QUBO
# --------------------------------------------------
def solve_nqueens(n, client):
    gen = VariableGenerator()
    x = gen.array("Binary", n, n)

    H = 0

    # Row constraints
    for i in range(n):
        H += (sum(x[i, j] for j in range(n)) - 1) ** 2

    # Column constraints
    for j in range(n):
        H += (sum(x[i, j] for i in range(n)) - 1) ** 2

    # Diagonals (top-left → bottom-right)
    for d in range(-n + 1, n):
        diag = []
        for i in range(n):
            j = i - d
            if 0 <= j < n:
                diag.append(x[i, j])
        if len(diag) > 1:
            H += sum(diag) * (sum(diag) - 1)

    # Diagonals (top-right → bottom-left)
    for s in range(2 * n - 1):
        diag = []
        for i in range(n):
            j = s - i
            if 0 <= j < n:
                diag.append(x[i, j])
        if len(diag) > 1:
            H += sum(diag) * (sum(diag) - 1)

    model = Model(H)

    start = time.time()
    result = solve(model, client)
    end = time.time()

    best = result.best

    return {
        "n": n,
        "energy": best.objective,
        "best_time": best.time.total_seconds(),
        "execution_time": result.execution_time.total_seconds(),
        "total_time": result.total_time.total_seconds(),
        "wall_time": end - start,
        "solution": best.values,
        "variables": x,
    }


# --------------------------------------------------
# MAIN
# --------------------------------------------------
if __name__ == "__main__":

    client = FixstarsClient()
    client.token = "AE/dWeqOQowYFzD628DM21bRIYFLzyNDCIK"
    client.parameters.timeout = 1000  # ms

    with open("results.txt", "w") as f:

        for n in Ns:
            print(f"Solving {n}-Queens...")
            res = solve_nqueens(n, client)

            f.write(f"N = {n}\n")
            f.write(f"Energy = {res['energy']}\n")
            f.write(f"Best solution time = {res['best_time']:.6f} s\n")
            f.write(f"Execution time = {res['execution_time']:.6f} s\n")
            f.write(f"Total time = {res['total_time']:.6f} s\n")
            f.write(f"Wall-clock time = {res['wall_time']:.6f} s\n")

            f.write("Board:\n")
            x = res["variables"]
            sol = res["solution"]
            for i in range(n):
                row = [str(int(sol[x[i, j]])) for j in range(n)]
                f.write(" ".join(row) + "\n")

            f.write("\n" + "-" * 40 + "\n\n")

    print("Done. Results saved in results.txt")
