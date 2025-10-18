#!/usr/bin/env python3
"""
シンプルな電卓プログラム
四則演算と履歴機能を備えています。
"""

class Calculator:
    def __init__(self):
        """電卓を初期化"""
        self.history = []
    
    def add(self, a, b):
        """加算"""
        result = a + b
        self._record(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """減算"""
        result = a - b
        self._record(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乗算"""
        result = a * b
        self._record(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除算"""
        if b == 0:
            raise ValueError("ゼロで除算できません")
        result = a / b
        self._record(f"{a} / {b} = {result}")
        return result
    
    def _record(self, operation):
        """計算履歴に記録"""
        self.history.append(operation)
    
    def get_history(self):
        """履歴を取得"""
        return self.history
    
    def clear_history(self):
        """履歴をクリア"""
        self.history = []
    
    def print_history(self):
        """履歴を表示"""
        if not self.history:
            print("履歴はありません")
            return
        print("\n=== 計算履歴 ===")
        for i, record in enumerate(self.history, 1):
            print(f"{i}. {record}")


def main():
    """メイン処理"""
    calc = Calculator()
    
    print("=== シンプル電卓 ===")
    print("コマンド: add, sub, mul, div, history, clear, exit\n")
    
    while True:
        try:
            command = input("コマンド> ").strip().lower()
            
            if command == "exit":
                print("電卓を終了します")
                break
            
            elif command == "history":
                calc.print_history()
            
            elif command == "clear":
                calc.clear_history()
                print("履歴をクリアしました")
            
            elif command in ["add", "sub", "mul", "div"]:
                a = float(input("最初の数値: "))
                b = float(input("次の数値: "))
                
                if command == "add":
                    result = calc.add(a, b)
                elif command == "sub":
                    result = calc.subtract(a, b)
                elif command == "mul":
                    result = calc.multiply(a, b)
                else:  # div
                    result = calc.divide(a, b)
                
                print(f"結果: {result}\n")
            
            else:
                print("不明なコマンドです。もう一度入力してください。\n")
        
        except ValueError as e:
            print(f"エラー: {e}\n")
        except Exception as e:
            print(f"入力エラー: {e}\n")


if __name__ == "__main__":
    main()
