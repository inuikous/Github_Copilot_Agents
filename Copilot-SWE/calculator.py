#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
シンプルな電卓プログラム
四則演算と履歴機能を提供します。
"""

import os

class Calculator:
    def __init__(self):
        """電卓の初期化"""
        self.history = []
    
    def add(self, a, b):
        """足し算"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """引き算"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """掛け算"""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """割り算"""
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def show_history(self):
        """計算履歴を表示"""
        if not self.history:
            print("計算履歴はありません。")
            return
        print("\n=== 計算履歴 ===")
        for i, calculation in enumerate(self.history, 1):
            print(f"{i}. {calculation}")
    
    def clear_history(self):
        """履歴をクリア"""
        self.history.clear()
        print("履歴をクリアしました。")

def main():
    """メイン関数"""
    calc = Calculator()
    
    while True:
        print("\n=== 電卓プログラム ===")
        print("1. 足し算")
        print("2. 引き算") 
        print("3. 掛け算")
        print("4. 割り算")
        print("5. 履歴表示")
        print("6. 履歴クリア")
        print("7. 終了")
        
        try:
            choice = input("\n操作を選択してください (1-7): ")
            
            if choice == "7":
                print("電卓プログラムを終了します。")
                break
            elif choice == "5":
                calc.show_history()
            elif choice == "6":
                calc.clear_history()
            elif choice in ["1", "2", "3", "4"]:
                a = float(input("最初の数値を入力してください: "))
                b = float(input("2番目の数値を入力してください: "))
                
                if choice == "1":
                    result = calc.add(a, b)
                elif choice == "2":
                    result = calc.subtract(a, b)
                elif choice == "3":
                    result = calc.multiply(a, b)
                elif choice == "4":
                    result = calc.divide(a, b)
                
                print(f"結果: {result}")
            else:
                print("無効な選択です。1-7の範囲で選択してください。")
                
        except ValueError as e:
            print(f"エラー: {e}")
        except Exception as e:
            print(f"予期しないエラーが発生しました: {e}")

if __name__ == "__main__":
    main()