# Exam of Special Lecture on Computer Science III ----- Samuele Moffa

This repository contains the implementation and experimental evaluation of several approaches to solve the **N-Queens problem**, developed as part of the *Special Lectures on Computer Science III* course.

## Repository Structure

The repository is organized into four main folders, each corresponding to a different approach:

.\
├── CP_boolean/\
├── CP_integer/\
├── LS/\
├── QUBO/\
├── graph.py

---

## 1. CP_boolean

Constraint Programming model using **Boolean variables and pseudo-Boolean constraints**, implemented in MiniZinc.

### Files
- `CP_boolean.mzn`  
  MiniZinc model of the N-Queens problem using \( n^2 \) Boolean variables.  
  Row, column, and diagonal constraints are expressed as linear pseudo-Boolean constraints.

- `script.ps1`  
  PowerShell script used to execute the MiniZinc model for multiple values of \( n \) and collect solver statistics.

- `results.txt`  
  Experimental results, including solver statistics and solution boards for different problem sizes.

---

## 2. CP_integer

Constraint Programming model using **integer variables and global constraints**, implemented in MiniZinc.

### Files
- `CP_integer.mzn`  
  MiniZinc model of the N-Queens problem using \( n \) integer variables, one per row, representing the column position of each queen.  
  The model uses global constraints such as `alldifferent` to enforce non-attacking conditions.

- `script.ps1`  
  PowerShell script used to run the model on multiple instances and collect performance statistics.

- `results.txt`  
  Experimental results, including solver statistics and solution boards for different problem sizes.

---

## 3. LS (Local Search)

Local search implementation based on the **Min-Conflicts heuristic**, as presented in Lecture 7.

### Files
- `LS.py`  
  Python implementation of a stochastic local search algorithm for the N-Queens problem, using random restarts and conflict minimization.

- `results.txt`  
  Experimental results, including number of restarts, number of steps, execution time, and final solutions for various values of \( n \).

---

## 4. QUBO

Quadratic Unconstrained Binary Optimization (QUBO) formulation of the N-Queens problem, solved using a **quantum-inspired annealing solver**.

### Files
- `QUBO.py`  
  Python script that constructs the QUBO model using the Fixstars Amplify SDK and solves it using the Fixstars Amplify Annealing Engine.

- `results.txt`  
  Experimental results, including solution energies, execution times, and decoded board configurations for different problem sizes.

---

## Additional file

`graph.py`
Python script for the graphs generation

## Notes

- All experiments were executed on the same machine to ensure a fair comparison.
- The reported runtimes correspond to the solver execution time unless otherwise specified.
- The complete analysis and comparison of the different approaches is presented in the accompanying project report.
