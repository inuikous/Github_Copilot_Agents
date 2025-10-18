#!/usr/bin/env python3
"""
シンプルな電卓プログラム
四則演算と履歴機能を提供する。
"""

import sys

# 履歴を格納するリスト
history = []

# 四則演算の関数群
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("ゼロ除算エラー: 0 で割ることはできません。")
    return a / b

# 式を解析して計算する

def calculate(expr):
    tokens = expr.strip().split()
    if len(tokens) != 3:
        raise ValueError("式の形式が正しくありません。例: 1 + 2")
    a_str, op, b_str = tokens
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise ValueError("数値を正しく入力してください。")

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    else:
        raise ValueError(f"未対応の演算子: {op}")

    # 履歴に追加
    history.append((expr, result))
    return result

# 履歴を表示する

def show_history():
    if not history:
        print("履歴がありません。")
        return
    print("=== 計算履歴 ===")
    for idx, (expr, res) in enumerate(history, start=1):
        print(f"{idx}: {expr} = {res}")
    print("================")

# メインループ
def main():
    print("シンプル電卓へようこそ。式を入力してください。\n終了するには 'exit' または 'quit' を入力、履歴表示には 'history' を入力。")
    while True:
        try:
            inp = input('> ')
        except (EOFError, KeyboardInterrupt):
            print('\n終了します。')
            break
        cmd = inp.strip().lower()
        if cmd in ('exit', 'quit'):
            print('終了します。')
            break
        if cmd == 'history':
            show_history()
            continue
        if not inp:
            continue
        try:
            res = calculate(inp)
            print(res)
        except Exception as e:
            print(f"エラー: {e}")

if __name__ == '__main__':
    main()
