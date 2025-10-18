# Calculator Guide

## Overview
This is a simple command-line calculator program written in Python. It supports basic arithmetic operations and maintains a history of calculations.

## Features
- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **History Tracking**: Keeps a record of all calculations performed in the current session
- **Error Handling**: Handles invalid inputs and division by zero
- **User-Friendly Interface**: Interactive prompts for easy use

## Requirements
- Python 3.x installed on your system
- No additional libraries required

## Installation
1. Ensure Python is installed. You can check by running `python --version` in your terminal.
2. Download or copy the `calculator.py` file to your desired directory.
3. Open a terminal and navigate to the directory containing `calculator.py`.

## How to Run
1. Open your command prompt or terminal.
2. Navigate to the folder where `calculator.py` is located.
3. Run the program with: `python calculator.py`
4. Follow the on-screen prompts.

## Usage Instructions
1. **Starting the Program**: Run `python calculator.py` to start the calculator.
2. **Selecting an Operation**:
   - Type `+` for addition
   - Type `-` for subtraction
   - Type `*` for multiplication
   - Type `/` for division
   - Type `history` to view past calculations
   - Type `exit` to quit the program
3. **Entering Numbers**: After selecting an operation, enter two numbers when prompted.
4. **Viewing Results**: The result will be displayed immediately after calculation.
5. **Viewing History**: Type `history` at any time to see a list of all previous calculations.
6. **Exiting**: Type `exit` to close the program.

## Examples
### Addition
```
Enter operation (+, -, *, /, history, exit): +
Enter first number: 5
Enter second number: 3
Result: 8.0
```

### Subtraction
```
Enter operation (+, -, *, /, history, exit): -
Enter first number: 10
Enter second number: 4
Result: 6.0
```

### Multiplication
```
Enter operation (+, -, *, /, history, exit): *
Enter first number: 7
Enter second number: 6
Result: 42.0
```

### Division
```
Enter operation (+, -, *, /, history, exit): /
Enter first number: 15
Enter second number: 3
Result: 5.0
```

### Division by Zero
```
Enter operation (+, -, *, /, history, exit): /
Enter first number: 10
Enter second number: 0
Result: Error: Division by zero
```

### Viewing History
```
Enter operation (+, -, *, /, history, exit): history
Calculation History:
1. 5.0 + 3.0 = 8.0
2. 10.0 - 4.0 = 6.0
```

## Tips
- Always enter valid numbers; the program will prompt for re-entry on invalid input.
- History is cleared when you exit the program.
- Use floating-point numbers for decimal calculations (e.g., 3.14).

## Troubleshooting
- **Program doesn't start**: Ensure Python is installed and the command is `python calculator.py` (or `python3` on some systems).
- **Invalid operation error**: Make sure to type the operation exactly as shown (+, -, *, /).
- **Division by zero**: The program prevents division by zero and displays an error message.

## License
This is a simple educational program. Feel free to modify and use as needed.