# Lockboxes Project

## Description
The Lockboxes project involves solving the problem of determining if all locked boxes can be opened given a series of keys found within those boxes. Each box may contain keys to other boxes, and the first box (index 0) is initially unlocked.

## Installation
To use the code in this project, ensure you have Python 3 installed on your machine.

1. Clone the repository:
   ```bash
   git clone https://github.com/harystyleseze/alx-interview.git
   ```
2. Navigate to the directory:
   ```bash
   cd alx-interview/0x01-lockboxes
   ```

## Usage
To run the project, execute the `main_0.py` script, which contains test cases for the `canUnlockAll` function:

```bash
chmod +x main_0.py  # Make the script executable
./main_0.py         # Run the script
```

## Function Prototype
```python
def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
```

## Example
Given the following input:

```python
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True
```

## Author
**Harrison Eze**  
GitHub: [harystyleseze](https://github.com/harystyleseze)

## License
This project is open source and available under the MIT License.
```
