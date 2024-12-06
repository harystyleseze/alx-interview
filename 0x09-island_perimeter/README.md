# 0x09. Island Perimeter

## Project Overview

The **Island Perimeter** project is part of the ALX Software Engineering program. In this project, the task is to write a function that calculates the perimeter of an island in a grid. The grid consists of water (represented by `0`s) and land (represented by `1`s). Each cell is a square with side length 1, and the grid is surrounded by water on all sides. The goal is to compute the perimeter of the island formed by the land cells (`1`s).

## Table of Contents

- [Author](#author)
- [Description](#description)
- [Task Requirements](#task-requirements)
- [File Structure](#file-structure)
- [Functionality](#functionality)
- [How to Run the Code](#how-to-run-the-code)
- [Test Cases](#test-cases)
- [Contributing](#contributing)
- [License](#license)

## Author

**Name**: Harrison Eze  
**Username**: harystyleseze  
**GitHub Repository**: [alx-interview](https://github.com/harystyleseze)  
**GitHub Profile**: [https://github.com/harystyleseze](https://github.com/harystyleseze)  

## Description

This project involves solving the problem of calculating the **perimeter of an island** in a 2D grid. Each land cell (`1`) is part of an island, and water cells (`0`) surround the island. The goal is to compute the perimeter of the island by counting the number of exposed edges of land cells. The task involves iterating over a grid, checking for neighboring cells, and calculating the exposed edges of the island.

### Problem Breakdown:
- The grid is rectangular, and the size does not exceed 100x100 cells.
- The grid is surrounded by water.
- Each land cell contributes to the perimeter based on its neighboring cells being either water (`0`) or out of bounds.

## Task Requirements

- Create a function `def island_perimeter(grid)` that returns the perimeter of the island described in the grid.
- **Input:**
  - `grid`: A list of lists of integers, where:
    - `0` represents water.
    - `1` represents land.
  - The grid is rectangular, and the width and height are not greater than 100.
- **Output:**
  - The function should return the perimeter of the island.
  
### Constraints:
- The grid is completely surrounded by water.
- There is only one island or no island at all.
- The island does not have lakes (water cells surrounded by land cells).

## File Structure

```bash
.
├── 0-island_perimeter.py
├── 0-main.py
└── README.md
```

- **0-island_perimeter.py**: Contains the solution to the Island Perimeter problem, specifically the function `island_perimeter(grid)`.
- **0-main.py**: A script that imports the `island_perimeter` function and tests it with an example grid.
- **README.md**: This file, which provides an overview of the project, instructions, and setup.

## Functionality

The function `island_perimeter(grid)` works by iterating over every cell in the grid:
1. For each land cell (`1`), it checks its four adjacent cells (up, down, left, and right).
2. If any adjacent cell is water (`0`) or out of bounds, it contributes to the perimeter.
3. The total perimeter is returned after iterating through the entire grid.

### Example:
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Expected Output: 12
```

## How to Run the Code

To run the code, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/harystyleseze/alx-interview.git
cd alx-interview/0x09-island_perimeter
```

2. Run the `0-main.py` file to test the solution:

```bash
python3 0-main.py
```

### Expected Output:
For the example input grid:
```python
[ [0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0] ]
```
The output will be:
```bash
12
```

## Test Cases

Here are some test cases to validate the implementation:

1. **Test Case 1** – A simple island:
   ```python
   grid = [
       [0, 1, 0],
       [0, 1, 0],
       [0, 1, 0]
   ]
   print(island_perimeter(grid))  # Expected Output: 8
   ```

2. **Test Case 2** – No island (only water):
   ```python
   grid = [
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]
   ]
   print(island_perimeter(grid))  # Expected Output: 0
   ```

3. **Test Case 3** – Island on the edge:
   ```python
   grid = [
       [1, 0],
       [1, 0]
   ]
   print(island_perimeter(grid))  # Expected Output: 6
   ```

## Contributing

1. Fork the repository
2. Create a new branch for your changes.
3. Commit your changes with a meaningful commit message.
4. Push the changes to your forked repository.
5. Submit a pull request describing your changes.

We welcome contributions from everyone! Please ensure your code adheres to the coding style guidelines provided in the project.

## License

This project is licensed under the MIT License.
