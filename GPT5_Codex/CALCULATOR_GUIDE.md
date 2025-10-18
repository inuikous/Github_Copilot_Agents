# CALCULATOR GUIDE

This guide explains how to run and use the command-line calculator bundled in calculator.py.

## Overview
- Provides addition, subtraction, multiplication, and division for decimal numbers.
- Stores up to the full session of calculations in chronological history.
- Offers quick recall of recent entries with an adjustable history length.

## Requirements
- Python 3.9 or newer (earlier versions with typing support also work).
- A terminal capable of running Python scripts.

## Launching
1. Open a terminal in the project directory.
2. Run: python calculator.py
3. Confirm the prompt displays '> '.

## Entering Expressions
- Use space separated input: number operator number.
- Supported operators: + - * /
- Numbers accept standard float syntax, e.g., 3, -0.5, 2.75e2.
- The result prints immediately and is added to history.

## History Commands
- Type history to show the last five results.
- Type history N (replace N with an integer) to pull that many entries.
- History prints oldest to newest within the requested slice.

## Session Control
- Type quit or exit to leave the program cleanly.
- Press Enter on an empty line to re-display the prompt without action.

## Examples
- 8 + 4
- 5.5 * 7
- -10 / 2
- history 3

## Error Handling
- Invalid formats trigger a helpful error message without ending the session.
- Division by zero is blocked with a clear warning.
- Non-numeric values must be corrected before retrying.

## Tips
- Combine with shell history to rerun frequent expressions quickly.
- Copy history output if you want to persist the session log.
- Use scientific notation for very large or small numbers.

## Troubleshooting
- If Python is not found, ensure it is installed and on your PATH.
- For locale issues, set the terminal encoding to UTF-8.
- If input freezes, press Ctrl+C to interrupt and restart.
