# Simple Calculator - 使用ガイド

このツールは、四則演算と履歴を備えたシンプルな電卓です。単発実行と対話モードの両方をサポートします。

## 特徴
- 四則演算: `+`, `-`, `*`, `/`
- 履歴: 実行結果をセッション内で保存し、`history` で表示、`clear` で消去
- エラー表示: 入力不正やゼロ除算はメッセージ表示

## 前提
- Python 3.8 以上がインストールされていること

## 単発実行 (Windows cmd)
以下はコマンドプロンプトでの例です。
```cmd
python calculator.py 2 + 3
python calculator.py 10 / 2
python calculator.py 7 * 8
python calculator.py 9 - 4
```

## 対話モード
引数なしで起動すると REPL が立ち上がります。
```cmd
python calculator.py
```
プロンプト `>` に次の形式で入力します。
```
<number> <op> <number>
```
例:
```
2 + 3
10 / 2
history
clear
exit
```

## コマンド一覧
- `history`: 履歴の表示
- `clear`: 履歴のクリア
- `exit`/`quit`: 終了

## 入力のルール
- トークンは空白区切りで3つ: 例 `12.5 * 4`
- 演算子は `+ - * /` のみ対応
- 数字は整数/小数どちらでも可

## エラー例
- `use: <number> <op> <number>`: トークンが3つでない
- `unsupported operator: ^`: 未対応の演算子
- `division by zero`: 0で割ろうとした

## 注意
- 履歴はプログラム実行中のみ保持され、終了すると消えます。
- 浮動小数演算のため、表示が丸められる場合があります。
