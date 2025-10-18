#!/usr/bin/env python3
"""
シンプルな電卓プログラム
機能:
- 四則演算（+ - * /）
- 計算の履歴を保持（最大100件）
- 履歴表示、履歴のクリア
- 対話モードおよびコマンドライン引数で式を評価

使い方は同ディレクトリの CALCULATOR_GUIDE.md を参照
"""

from collections import deque
import operator
import sys
import ast

MAX_HISTORY = 100

# 安全な演算ノードを許可するためのAST評価
ALLOWED_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Num,
    ast.Load,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Mod,
    ast.Pow,
    ast.USub,
    ast.UAdd,
    ast.Constant,
    ast.Tuple,
    ast.List,
)


def safe_eval(expr: str) -> float:
    """文字列の数式を安全に評価して数値を返す。
    サポート: + - * / % ** と括弧。変数や関数呼び出しは許可しない。
    """
    try:
        node = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError("無効な式") from e

    for n in ast.walk(node):
        if not isinstance(n, ALLOWED_NODES):
            raise ValueError(f"許可されていない構文: {type(n).__name__}")

    # ast.Expression の body を評価
    code = compile(node, "<safe_eval>", "eval")
    try:
        return eval(code, {"__builtins__": None}, {})
    except Exception as e:
        raise ValueError("評価エラー: " + str(e)) from e


class Calculator:
    def __init__(self, max_history: int = MAX_HISTORY):
        self.history = deque(maxlen=max_history)

    def calculate(self, expr: str) -> float:
        result = safe_eval(expr)
        self.history.append((expr, result))
        return result

    def show_history(self) -> None:
        if not self.history:
            print("履歴はありません")
            return
        for i, (expr, res) in enumerate(self.history, start=1):
            print(f"{i}: {expr} = {res}")

    def clear_history(self) -> None:
        self.history.clear()
        print("履歴をクリアしました")


def repl(calc: Calculator) -> None:
    print("シンプル電卓 — 式を入力してください。:q で終了、:h 履歴、:c クリア")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        if line in (":q", "quit", "exit"):
            break
        if line in (":h", "history"):
            calc.show_history()
            continue
        if line in (":c", "clear"):
            calc.clear_history()
            continue
        try:
            res = calc.calculate(line)
            print(res)
        except ValueError as e:
            print("エラー:", e)


def main(argv):
    calc = Calculator()
    # コマンドライン引数があれば式を評価して終了
    if len(argv) > 1:
        expr = " ".join(argv[1:])
        try:
            res = calc.calculate(expr)
            print(res)
        except ValueError as e:
            print("エラー:", e)
        return

    # 対話モード
    repl(calc)


if __name__ == "__main__":
    main(sys.argv)
