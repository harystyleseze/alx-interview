# N Queens

## Overview

The **N Queens** problem is a classical puzzle in computer science and mathematics. It involves placing **N queens** on an **NN chessboard** such that no two queens can attack each other. A queen in chess can move horizontally, vertically, or diagonally, so the task is to ensure no two queens share the same row, column, or diagonal.

This project provides a solution to the N Queens puzzle using the **backtracking algorithm**. The program generates all valid solutions to the problem and prints each solution in a specific format.

## Author

**Harrison Eze**  
GitHub: [harystyleseze](https://github.com/harystyleseze)

## Requirements

- Python 3.x
- The program should be executed from the command line.

## Usage

### How to Run the Program

1. Clone this repository:
   ```bash
   git clone https://github.com/harystyleseze/alx-interview.git
   cd alx-interview/0x05-nqueens
   ```

2. Make the script executable:
   ```bash
   chmod +x 0-nqueens.py
   ```

3. Run the script with the desired number `N` (the size of the chessboard):
   ```bash
   ./0-nqueens.py <N>
   ```

   Where `<N>` is an integer greater than or equal to 4. The program will print all possible solutions to the N Queens puzzle.

### Example:

For `N = 4`:
```bash
./0-nqueens.py 4
```

Expected output:
```plaintext
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

For `N = 6`:
```bash
./0-nqueens.py 6
```

Expected output:
```plaintext
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### Input Validation

- If no argument is provided, the program will print:
  ```plaintext
  Usage: nqueens N
  ```
  
- If the provided argument is not a number, the program will print:
  ```plaintext
  N must be a number
  ```

- If `N` is less than 4, the program will print:
  ```plaintext
  N must be at least 4
  ```

## Files

- `0-nqueens.py`: Python script that solves the N Queens problem using the backtracking algorithm.

## Algorithm Explanation

The N Queens problem is solved using **backtracking**:

1. We place a queen in a row and check if it is safe (i.e., not under attack by any previously placed queens).
2. If the queen is placed safely, we recursively try to place a queen in the next row.
3. If we reach the last row, a valid solution has been found, and we add the solution to the list.
4. If placing the queen leads to a conflict, we backtrack and try placing the queen in the next column.
5. This process continues until all solutions are found.

Each solution is represented as a list of queen positions where each element of the list is a pair `[row, column]`.

## Constraints

- The value of `N` must be an integer greater than or equal to 4, as placing fewer than 4 queens on a board results in trivial solutions.

## Example Output Format

The output for a solution to the N Queens problem is a list of pairs representing the positions of queens on the chessboard:

- Each pair `[i, j]` represents a queen placed at row `i` and column `j`.
- Multiple solutions are printed, with each solution on a new line.

### Example:

For `N = 4`, the possible solutions are:

```plaintext
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

For `N = 6`, the possible solutions are:

```plaintext
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Acknowledgments

- The N Queens problem is a classic puzzle that has been widely studied in computer science.
- Special thanks to the ALX program for encouraging the development of algorithmic problem-solving skills.

```
