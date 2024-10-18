# Minimum Operations

## Project Overview
The **Minimum Operations** project focuses on a simple text manipulation problem involving the operations "Copy All" and "Paste". The objective is to determine the fewest number of operations required to generate exactly \( n \) characters of "H" in a text file, starting with a single character "H".

## Table of Contents
- [Author](#author)
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Examples](#examples)
- [Implementation](#implementation)
- [License](#license)

## Author
**Name:** Harrison Eze  
**Username:** harystyleseze  
**GitHub Profile:** [harystyleseze](https://github.com/harystyleseze)  
**GitHub Repository:** [alx-interview](https://github.com/harystyleseze/alx-interview)  

## Description
The task is to implement a function that calculates the minimum number of operations needed to generate exactly \( n \) "H" characters. The function must follow these specifications:

### Function Prototype
```python
def minOperations(n)
```

### Return Value
- Returns an integer representing the minimum number of operations needed to reach \( n \) characters.
- If \( n \) is impossible to achieve, return 0.

### Operations Allowed
1. **Copy All**: Copies all characters currently in the file to a clipboard.
2. **Paste**: Pastes the contents of the clipboard to the file.

## Requirements
- Python 3.4.3 or later
- Ubuntu 20.04 LTS

## Usage
To use the `minOperations` function, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/harystyleseze/alx-interview.git
   ```

2. Navigate to the project directory:
   ```bash
   cd alx-interview/0x02-minimum_operations
   ```

3. Run the main test file:
   ```bash
   ./0-main.py
   ```

## Examples
Here are some example usages of the `minOperations` function:

```python
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 4

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 7

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 6
```

### Detailed Example
For \( n = 9 \):
```
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
```

## Implementation
The function is implemented in `0-minoperations.py`. The implementation uses a loop to simulate the copy and paste operations and calculates the minimum operations required.

### Sample Implementation
```python
#!/usr/bin/python3
'''Minimum Operations python3 challenge'''

def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted_chars = 1  # how many chars in the file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        if clipboard == 0:
            clipboard = pasted_chars
            counter += 1

        if pasted_chars == 1:
            pasted_chars += clipboard
            counter += 1
            continue

        remaining = n - pasted_chars
        if remaining < clipboard:
            return 0

        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2

    return counter if pasted_chars == n else 0
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
