# 0x03. Log Parsing

## Author
**Harrison Eze**  
[GitHub Profile](https://github.com/harystyleseze)

## Project Overview

The **0x03. Log Parsing** project is designed to provide a practical understanding of parsing log files and processing data streams in real-time using Python. This project focuses on reading from standard input, extracting meaningful information from log entries, and calculating relevant metrics.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Functionality](#functionality)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Requirements

To run this project, you will need:
- Python 3.x installed on your machine.
- Basic knowledge of Python programming, including handling file I/O, data processing, and signal handling.

## File Structure

```
0x03-log_parsing/
├── 0-generator.py   # Script to generate random log entries
├── 0-stats.py       # Script to parse logs and compute metrics
└── README.md        # Project documentation
```

## Usage

1. **Generate Log Entries**: Use the `0-generator.py` script to simulate log entries.
2. **Parse Logs**: Pipe the output of the generator script to `0-stats.py` to process and compute metrics.

### Command to Run

```bash
./0-generator.py | ./0-stats.py
```

## Functionality

The `0-stats.py` script performs the following tasks:

- Reads log entries from standard input (stdin).
- Parses each log entry to extract the IP address, date, status code, and file size.
- Computes the total file size of processed logs.
- Counts occurrences of specific HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).
- Outputs the total file size and status code counts every 10 lines or upon keyboard interruption (CTRL + C).

## Example Output

Here’s an example of what the output might look like when running the scripts:

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
...
^CFile size: 17146
200: 4
301: 3
...
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or enhancements, feel free to submit a pull request or open an issue in the repository.

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to use and modify it as per your needs.
