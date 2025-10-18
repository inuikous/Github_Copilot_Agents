"""
シンプル電卓プログラム
四則演算と履歴機能を提供します
"""

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """加算"""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """減算"""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乗算"""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除算"""
        if b == 0:
            raise ValueError("0で割ることはできません")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
    
    def _add_to_history(self, operation):
        """履歴に追加"""
        self.history.append(operation)
    
    def show_history(self):
        """履歴を表示"""
        if not self.history:
            print("履歴はありません")
            return
        print("\n=== 計算履歴 ===")
        for i, record in enumerate(self.history, 1):
            print(f"{i}. {record}")
    
    def clear_history(self):
        """履歴をクリア"""
        self.history.clear()
        print("履歴をクリアしました")

def main():
    calc = Calculator()
    
    print("=" * 40)
    print("シンプル電卓プログラム")
    print("=" * 40)
    
    while True:
        print("\n[1] 加算  [2] 減算  [3] 乗算  [4] 除算")
        print("[5] 履歴表示  [6] 履歴クリア  [0] 終了")
        
        choice = input("\n選択してください: ").strip()
        
        if choice == "0":
            print("電卓を終了します")
            break
        
        if choice == "5":
            calc.show_history()
            continue
        
        if choice == "6":
            calc.clear_history()
            continue
        
        if choice not in ["1", "2", "3", "4"]:
            print("無効な選択です")
            continue
        
        try:
            num1 = float(input("1つ目の数値: "))
            num2 = float(input("2つ目の数値: "))
            
            if choice == "1":
                result = calc.add(num1, num2)
            elif choice == "2":
                result = calc.subtract(num1, num2)
            elif choice == "3":
                result = calc.multiply(num1, num2)
            elif choice == "4":
                result = calc.divide(num1, num2)
            
            print(f"\n結果: {result}")
            
        except ValueError as e:
            print(f"エラー: {e}")
        except Exception as e:
            print(f"予期しないエラー: {e}")

if __name__ == "__main__":
    main()
