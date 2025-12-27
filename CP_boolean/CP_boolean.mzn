%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% N-Queens with Boolean variables and pseudo-Boolean constraints
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

int: n;  % dimension of the board

set of int: ROWS = 1..n;
set of int: COLS = 1..n;

% Boolean variables:
% x[i,j] = 1 if there is a queen in cell (i,j), 0 otherwise
array[ROWS, COLS] of var 0..1: x;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Row constraints
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
constraint
  forall(i in ROWS) (
    sum(j in COLS)(x[i,j]) = 1
  );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Column constraints
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
constraint
  forall(j in COLS) (
    sum(i in ROWS)(x[i,j]) = 1
  );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Main diagonals (i - j)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
constraint
  forall(k in -(n-1)..(n-1)) (
    sum(i in ROWS, j in COLS where i - j = k)(x[i,j]) <= 1
  );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Secondary diagonals (i + j)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
constraint
  forall(k in 2..(2*n)) (
    sum(i in ROWS, j in COLS where i + j = k)(x[i,j]) <= 1
  );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Solve
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
solve satisfy;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Output
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
output [
  if j = 1 then "\n" else "" endif ++
  (if fix(x[i,j]) = 1 then "Q" else "." endif)
  | i in ROWS, j in COLS
];
