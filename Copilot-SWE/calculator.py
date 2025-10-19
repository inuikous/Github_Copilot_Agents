#!/usr/bin/env python3
"""
シンプルな電卓（REPL）

機能:
 - 四則演算（+ - * /）
 - 式の評価（括弧、浮動小数点、負の数対応）
 - 計算履歴（最新10件）
"""
from collections import deque
import ast
import operator
import sys


class CalcError(Exception):
    pass


class _Evaluator(ast.NodeVisitor):
    """AST を検査して安全に式を評価する。"""
    ALLOWED_OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def visit(self, node):
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        return super().visit(node)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)
        if op_type in self.ALLOWED_OPERATORS:
            try:
                return self.ALLOWED_OPERATORS[op_type](left, right)
            except ZeroDivisionError:
                raise CalcError("ゼロ除算")
        raise CalcError("許可されていない演算子")

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        op_type = type(node.op)
        if op_type in self.ALLOWED_OPERATORS:
            return self.ALLOWED_OPERATORS[op_type](operand)
        raise CalcError("許可されていない単項演算子")

    def visit_Num(self, node):
        return node.n

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            return node.value
        raise CalcError("数値以外は許可されていません")

    def generic_visit(self, node):
        raise CalcError(f"許可されていない構文: {type(node).__name__}")


def evaluate_expression(expr: str):
    """式を評価して結果（float または int）を返す。

    Raises CalcError on invalid expressions.
    """
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise CalcError("文法エラー") from e
    evaluator = _Evaluator()
    return evaluator.visit(tree)


def main():
    print("シンプル電卓 - 終了: exit, 履歴: history, クリア: clear")
    history = deque(maxlen=10)
    while True:
        try:
            s = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\n終了')
            return

        if not s:
            continue
        if s.lower() in ("exit", "quit"):
            print("終了")
            return
        if s.lower() == "history":
            if not history:
                print("履歴はありません")
                continue
            for i, (expr, res) in enumerate(history, 1):
                print(f"{i}: {expr} = {res}")
            continue
        if s.lower() == "clear":
            history.clear()
            print("履歴をクリアしました")
            continue

        try:
            result = evaluate_expression(s)
        except CalcError as e:
            print("エラー:", e)
            continue
        # 整数のときは整数として表示
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(result)
        history.append((s, result))


if __name__ == "__main__":
    main()
