#!/usr/bin/env python3

"""シンプルな電卓プログラム

四則演算（+ - * /）と計算履歴機能を実装しています。
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b


def main():
    history = []
    print("シンプルな電卓へようこそ。")
    print("使用方法: 数値 演算子 数値 と入力してください。例: 3 + 4")
    print("履歴を見るには 'history'、終了するには 'exit' を入力してください。")
    
    while True:
        inp = input("\n入力: ")
        if inp.strip().lower() == 'exit':
            print("電卓を終了します。")
            break
        elif inp.strip().lower() == 'history':
            print("\n計算履歴:")
            for record in history:
                print(record)
            continue
        
        try:
            parts = inp.split()
            if len(parts) != 3:
                print("入力形式が正しくありません。例: 3 + 4")
                continue
            a, op, b = parts
            a = float(a)
            b = float(b)
            
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print("不明な演算子です。")
                continue
            
            expression = f"{a} {op} {b} = {result}"
            print(expression)
            history.append(expression)
        except Exception as e:
            print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
