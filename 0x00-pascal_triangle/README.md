# Pascal's Triangle - ALX Interview Preparation

This project is part of the **ALX Interview Preparation** series and focuses on implementing **Pascal's Triangle** using Python.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Pascal's Triangle](#pascals-triangle)
3. [Requirements](#requirements)
4. [File Descriptions](#file-descriptions)
5. [How to Run](#how-to-run)
6. [Example Output](#example-output)
7. [Author](#author)

---

## Project Overview

The goal of this project is to implement a Python function that generates Pascal's Triangle for a given number of rows, `n`. This triangle is widely used in combinatorics and represents the coefficients in the binomial expansion.

---

## Pascal's Triangle

Pascal's Triangle is a triangular array where the values in each row are calculated based on the values from the previous row. Each number is the sum of the two numbers directly above it.

Example of Pascal’s Triangle for `n = 5`:
```
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
```

### Key Properties
- The first and last value in each row is always `1`.
- Every other value in the row is the sum of the two values directly above it in the previous row.

---

## Requirements

- Python 3.x
- Your script should be executable in a Unix-based terminal (Linux/MacOS).
- The function should:
  - Return a list of lists of integers representing Pascal’s Triangle.
  - Return an empty list if `n <= 0`.
  - Assume `n` will always be an integer.

---

## File Descriptions

- **0-pascal_triangle.py**: Contains the `pascal_triangle(n)` function which generates the Pascal's Triangle.
- **0-main.py**: A test script that prints the Pascal's Triangle for a given `n`.
- **README.md**: This documentation file explaining the project.

---

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/alx-interview.git
   cd alx-interview/0x00-pascal_triangle
   ```

2. **Run the test script**:
   To test the implementation with `n = 5`, execute the following command:
   ```bash
   $ python3 0-main.py
   ```

3. **Expected Output**:
   The script will print the Pascal's Triangle as follows:
   ```
   [1]
   [1,1]
   [1,2,1]
   [1,3,3,1]
   [1,4,6,4,1]
   ```

---

## Example Output

Here’s an example output when generating Pascal’s Triangle for `n = 5`:

```bash
$ python3 0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

---

## Author

- **Your Name** - [GitHub](https://github.com/YOUR_USERNAME)

```

### Instructions for Updating:
- Replace `YOUR_USERNAME` with your actual GitHub username.
- Customize the **Author** section if needed.
- Update any other sections to reflect your project details.

This `README.md` provides an overview, setup instructions, and an example of the output, helping users understand your Pascal’s Triangle project.
