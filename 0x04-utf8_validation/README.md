# UTF-8 Validation Project

## Author
**Harrison Eze**  
[GitHub Profile](https://github.com/harystyleseze)  
Username: harystyleseze

## Project Overview
This project implements a method to validate whether a given dataset represents a valid UTF-8 encoding. The method checks byte sequences to ensure they adhere to UTF-8 standards, which allow characters to be represented using 1 to 4 bytes.

## Requirements
- Python 3.4.3 or higher
- Ubuntu 20.04 LTS

## Function Prototype
```python
def validUTF8(data):
```

## Input
- `data`: A list of integers, where each integer represents a byte of data.

## Output
- Returns `True` if the data is a valid UTF-8 encoding, else returns `False`.

## UTF-8 Encoding Rules
- **1-byte characters**: `0xxxxxxx`
- **2-byte characters**: `110xxxxx 10xxxxxx`
- **3-byte characters**: `1110xxxx 10xxxxxx 10xxxxxx`
- **4-byte characters**: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/harystyleseze/alx-interview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-interview/0x04-utf8_validation
   ```
3. Run the provided test script to validate your implementation:
   ```bash
   chmod +x 0-main.py  # Make the script executable
   ./0-main.py         # Execute the test script
   ```

## Example
### Input
```python
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## License
This project is open source and available under the MIT License.

## Acknowledgments
- Special thanks to the ALX program for providing this opportunity to learn and implement UTF-8 encoding validation.

## Contact
For any questions or feedback, please reach out via my [GitHub profile](https://github.com/harystyleseze).
