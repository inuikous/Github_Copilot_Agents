#!/usr/bin/env python3
"""Simple command-line calculator with history tracking."""

from typing import List


class Calculator:
    def __init__(self) -> None:
        self.history: List[str] = []

    def _record(self, expression: str, result: float) -> float:
        self.history.append(f"{expression} = {result}")
        return result

    def add(self, a: float, b: float) -> float:
        return self._record(f"{a} + {b}", a + b)

    def subtract(self, a: float, b: float) -> float:
        return self._record(f"{a} - {b}", a - b)

    def multiply(self, a: float, b: float) -> float:
        return self._record(f"{a} * {b}", a * b)

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self._record(f"{a} / {b}", a / b)

    def last_entries(self, count: int = 5) -> List[str]:
        return self.history[-count:]


def evaluate(calc: Calculator, lhs: float, operator: str, rhs: float) -> float:
    if operator == "+":
        return calc.add(lhs, rhs)
    if operator == "-":
        return calc.subtract(lhs, rhs)
    if operator == "*":
        return calc.multiply(lhs, rhs)
    if operator == "/":
        return calc.divide(lhs, rhs)
    raise ValueError("Supported operators are +, -, *, /.")


def parse_expression(text: str) -> List[str]:
    tokens = text.split()
    if len(tokens) != 3:
        raise ValueError("Use format: <number> <operator> <number>.")
    return tokens


def main() -> None:
    calc = Calculator()
    print("Enter expressions like '2 + 2'. Type 'history [n]' or 'quit'.")
    while True:
        raw = input("> ").strip()
        if not raw:
            continue
        lower = raw.lower()
        if lower in {"quit", "exit"}:
            print("Goodbye!")
            break
        if lower.startswith("history"):
            parts = raw.split()
            count = int(parts[1]) if len(parts) > 1 else 5
            for entry in calc.last_entries(count):
                print(entry)
            continue
        try:
            left_text, op, right_text = parse_expression(raw)
            result = evaluate(calc, float(left_text), op, float(right_text))
            print(result)
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
