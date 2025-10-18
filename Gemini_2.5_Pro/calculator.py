# -*- coding: utf-8 -*-

def calculate():
    """
    シンプルな電卓機能を提供する関数。
    四則演算と計算履歴の表示が可能です。
    """
    history = []
    print("シンプルな電卓へようこそ！")
    print("計算式を入力してください (例: 1 + 1)")
    print("'history' と入力すると履歴が表示されます。")
    print("'quit' と入力すると終了します。")

    while True:
        try:
            expression = input(">>> ")

            if expression.lower() in ['quit', 'exit']:
                print("電卓を終了します。ご利用ありがとうございました。")
                break

            if expression.lower() == 'history':
                if not history:
                    print("計算履歴はありません。")
                else:
                    print("\n--- 計算履歴 ---")
                    for i, record in enumerate(history, 1):
                        print(f"{i}: {record}")
                    print("----------------\n")
                continue

            # セキュリティのリスクを考慮し、入力は限定的な文字のみ許可
            allowed_chars = "0123456789+-*/(). "
            if not all(char in allowed_chars for char in expression):
                raise ValueError("無効な文字が含まれています。")

            # eval() は便利ですが、信頼できない入力を評価すると危険なため注意
            result = eval(expression)
            
            record = f"{expression} = {result}"
            history.append(record)
            print(f"結果: {result}")

        except ZeroDivisionError:
            print("エラー: 0で割ることはできません。")
        except (SyntaxError, NameError):
            print("エラー: 計算式が正しくありません。もう一度入力してください。")
        except ValueError as ve:
            print(f"エラー: {ve}")
        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    calculate()
