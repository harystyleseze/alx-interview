# 0x0A. Prime Game

## Description
The Prime Game project is part of the ALX Software Engineering program, and it is designed to solve a prime number problem using Python. The task consists of simulating a game between two players, Ben and Maria, who alternate turns in picking prime numbers from a list. The goal is to determine the winner of the game based on the number of primes available for each player to choose from.

### Project Folder Structure:
- **Directory**: `0x0A-primegame`
- **Files**:
  - `0x0A-primegame.py` - The main script that solves the problem.

## Task

In this task, players are given a list of numbers and must take turns choosing primes. The winner is determined based on who has the most successful rounds. If both players win an equal number of rounds, the game ends in a draw.

The project involves implementing a function `isWinner(x, nums)` which simulates a series of rounds. Each round is played on a list of prime numbers up to a given number. If the number of primes in that round is odd, Maria wins, while if it's even, Ben wins. The function returns the name of the player who wins the most rounds.

## Requirements

### Python 3
- The script is written in Python 3 and requires Python 3.x to run.
- You can check your Python version by running:
  ```bash
  python3 --version
  ```

### Dependencies:
- No external dependencies are required for this task. You can run the code with a standard Python 3 installation.

## Functions

### 1. `sieve_of_eratosthenes(n)`
This function generates a list of prime numbers up to the number `n` using the Sieve of Eratosthenes algorithm. The sieve is an efficient way to generate all primes less than or equal to `n`.

**Arguments**:
- `n` (int): The upper limit to generate primes.

**Returns**:
- A list of prime numbers up to `n` (inclusive).
- `None` if `n` is less than 2 or not an integer.

### 2. `isWinner(x, nums)`
This function simulates a game of primes between two players, Ben and Maria, based on the number of primes up to various values given in `nums`.

**Arguments**:
- `x` (int): The number of rounds.
- `nums` (list of int): A list of integers, where each integer represents the upper bound for that round.

**Returns**:
- `"Ben"`: If Ben wins the most rounds.
- `"Maria"`: If Maria wins the most rounds.
- `None`: If no one wins or in case of an error.

## Usage

### Example:
```python
result = isWinner(2, [10, 20])
print(result)  # Output: "Ben" or "Maria" depending on the input.
```

### Explanation:
- In this example, `isWinner` runs two rounds:
  1. The first round uses `n = 10`, and the number of primes up to 10 is 4 (even, so Ben wins).
  2. The second round uses `n = 20`, and the number of primes up to 20 is 8 (even, so Ben wins).
- Since Ben wins both rounds, the result will be `"Ben"`.

## Contributions

Contributions to this repository are welcome. If you have suggestions for improvements or enhancements, feel free to fork the repository, make your changes, and submit a pull request.

## Author

- **Username**: harystyleseze
- **Full Name**: Harrison Eze
- **GitHub Repository**: [alx-interview](https://github.com/harystyleseze/alx-interview)
- **GitHub Profile**: [harystyleseze](https://github.com/harystyleseze)

## License

This project is open-source and available under the [MIT License](LICENSE).
