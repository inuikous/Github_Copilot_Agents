#!/usr/bin/env python3
import sys

HISTORY = []

def calculate(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0: raise ZeroDivisionError("division by zero")
        return a / b
    raise ValueError(f"unsupported operator: {op}")

def parse(expr):
    t = expr.strip().split()
    if len(t) != 3: raise ValueError("use: <number> <op> <number>")
    a, op, b = t[0], t[1], t[2]
    return float(a), op, float(b)

def repl():
    print("Simple Calculator - enter: <a> <op> <b>")
    print("Commands: history, clear, exit")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print(); break
        if not line: continue
        low = line.lower()
        if low in ("exit","quit"): break
        if low == "history":
            if not HISTORY: print("(no history)")
            else:
                for i, h in enumerate(HISTORY, 1): print(f"{i}: {h}")
            continue
        if low == "clear": HISTORY.clear(); print("history cleared"); continue
        try:
            a, op, b = parse(line)
            res = calculate(a, op, b)
            out = f"{a} {op} {b} = {res}"
            HISTORY.append(out)
            print(out)
        except Exception as e:
            print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        try:
            a, op, b = parse(expr)
            print(calculate(a, op, b))
        except Exception as e:
            print(f"Error: {e}"); sys.exit(1)
    else:
        repl()

if __name__ == "__main__":
    main()
