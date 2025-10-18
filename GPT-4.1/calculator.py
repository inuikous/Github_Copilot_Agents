import sys

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self._add_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._add_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self._add_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self._add_history(f"{a} / {b} = Error (division by zero)")
            return "Error: Division by zero"
        result = a / b
        self._add_history(f"{a} / {b} = {result}")
        return result

    def _add_history(self, entry):
        self.history.append(entry)
        if len(self.history) > 10:
            self.history.pop(0)

    def show_history(self):
        print("--- Calculation History ---")
        for entry in self.history:
            print(entry)
        print("--------------------------")

def main():
    calc = Calculator()
    print("シンプル電卓へようこそ！\n'help'で使い方を表示します。'exit'で終了。")
    while True:
        cmd = input("> ").strip()
        if cmd == "exit":
            break
        elif cmd == "help":
            print("使い方: [演算子] [数値1] [数値2] 例: add 2 3")
            print("演算子: add, sub, mul, div, history, exit")
        elif cmd == "history":
            calc.show_history()
        else:
            parts = cmd.split()
            if len(parts) != 3:
                print("コマンド形式が正しくありません。")
                continue
            op, a, b = parts
            try:
                a = float(a)
                b = float(b)
            except ValueError:
                print("数値を入力してください。")
                continue
            if op == "add":
                print(calc.add(a, b))
            elif op == "sub":
                print(calc.subtract(a, b))
            elif op == "mul":
                print(calc.multiply(a, b))
            elif op == "div":
                print(calc.divide(a, b))
            else:
                print("不明な演算子です。")

if __name__ == "__main__":
    main()
