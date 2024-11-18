# 0x07 - Rotate 2D Matrix

## Author:
- **Name**: Harrison Eze
- **Username**: harystyleseze
- **GitHub Profile**: [https://github.com/harystyleseze](https://github.com/harystyleseze)

## Project Description:
This project focuses on rotating a square matrix (2D matrix) 90 degrees clockwise. The task is to implement an in-place matrix rotation function that modifies the original matrix without creating any additional data structures. 

### Task Overview:
- **Task**: Rotate a given `n x n` 2D matrix 90 degrees clockwise.
- **Function Signature**: `def rotate_2d_matrix(matrix):`
- **Constraints**: 
  - The matrix is guaranteed to have 2 dimensions and will not be empty.
  - You must modify the matrix in place (do not return a new matrix).

### Example:
Given the input matrix:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

After applying the `rotate_2d_matrix` function, the output will be:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## File Structure:
The project contains the following files:

- `0-rotate_2d_matrix.py`: Python file implementing the function to rotate the matrix 90 degrees.
- `main_0.py`: A test script that demonstrates how the function works.
- `README.md`: This file.

## How to Run:

1. **Clone the repository:**
   To get started, clone the repository from GitHub:
   ```bash
   git clone https://github.com/harystyleseze/alx-interview.git
   cd alx-interview/0x07-rotate_2d_matrix
   ```

2. **Make the script executable:**
   Ensure the Python script is executable by running:
   ```bash
   chmod +x 0-rotate_2d_matrix.py
   ```

3. **Run the test script:**
   You can test the matrix rotation by running the provided test script (`main_0.py`):
   ```bash
   ./main_0.py
   ```

4. **Expected Output:**
   After running the script, you should see the matrix rotated 90 degrees clockwise. The output for the test case will look like:

   ```python
   [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]
   ```

## Function Details:

### `rotate_2d_matrix(matrix)`
Rotates a square matrix in place by 90 degrees clockwise. The matrix is modified directly without returning a new matrix.

- **Parameters**: 
  - `matrix` (List[List[int]]): A square matrix (2D list) of integers.
  
- **Returns**: 
  - Nothing. The matrix is rotated in place.
  
- **Complexity**:
  - **Time Complexity**: O(n^2), where `n` is the number of rows (or columns) in the matrix, as each element is visited once.
  - **Space Complexity**: O(1), as the matrix is modified in place without using extra space.

### Example Usage:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

### Expected Output:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Notes:
- The solution performs the rotation by processing the matrix layer by layer, starting from the outermost layer and moving inward.
- Each layer is rotated in place by swapping four elements at a time.
  
## Project Goals:
This project helps in understanding matrix manipulations, particularly rotating matrices in place. It is useful for improving problem-solving skills, especially in technical interviews, as rotating a matrix is a common interview question.

## License:
This project is open-source, and you are free to use it under the terms of the MIT license.

## Acknowledgments:
- Special thanks to the ALX program for providing the problem statement and resources for learning.
- Thanks to the contributors and open-source community for providing resources and solutions related to matrix manipulation and algorithm design.

## Contact:
- **GitHub Profile**: [https://github.com/harystyleseze](https://github.com/harystyleseze)
- **Email**: [harystyleseze@gmail.com] (harystyleseze@gmail.com)

---

Happy coding!
