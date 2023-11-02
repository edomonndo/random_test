# random_test

競技プログラミング用にランダムテストをします．

## ファイル構成

ファイル名の後ろにアスタリスク(*)がついたファイルは，問題に合わせて変更が必要なファイルです．

1. `lib.py`: テストケース作成用の関数を保存しています．
2. `gen_testcase.py`*: 実際の問題に合わせてテストケースを作成するスクリプトです．
3. `main.py`*: コンテストで使用するプログラムです．
4. `naive.py`*: コンテストで使用するプログラムと比較するためのプログラムです．通常は，実行速度が遅い愚直解を書くことになります．
5. `settings.py`*: テストケースの数や，実行コマンドなどの設定値を定義します．Python以外の言語で実行する場合や，Windows環境で実行する場合には，変更が必要です．
6. `judge.py`: テストする解法と愚直解を比較します．結果が異なる場合，そのときのテストケースのファイル名を出力します．

## 実行コマンドの変更

作者はPython3(Mac)で作業しているため，実行コマンドは`python3 hoge.py`となっています．Windows環境の方は，`settings.py`の`naive_command`と`main_command`を`python hoge.py`のように変更してください．
Python以外の言語でテストする場合は，`settings.py`の`naive_command`と`main_command`を各言語に合わせて変更してください．

なお,`naive_command`と`main_command`の後ろにつける標準入出力のファイル指定は`judge.py`の中で実行コマンドの後ろに` < ./in/0000.txt > ./out/0000.txt`のように文字列を追加しています．

## テストケース作成用の関数

事前に準備されているいくつかの関数を紹介します．

### 配列(Listクラス)

#### 配列を作成する

長さ$n$の配列を作成します．
配列の値はmin_value以上，max_value未満の値からランダムで選ばれます．is_uniqueがtrueだと値は配列の中で一意になります．

```
List.gen_list(n, min_value = 0, max_value = 10**9, is_unique = False)
```

#### 順列を作成する．

長さ$n$の順列を作成します．
is_1indexがtrueだと値は[1,n+1), falseだと[0,n)の範囲となります．

```
List.gen_permutation(n, is_1index = False)
```

### 無向グラフ(UndirectedGraphクラス)

#### 共通の変数

$n$: 頂点の数, $m$: 辺の数  
is1index: trueで頂点番号を[1,n+1), falseで[0,n)で出力します．

#### 重みなしグラフの辺を作成する．

```
UndirectedGraph.gen_edges(n, m, is1index = False)
```

#### 重みありグラフの辺を作成する．

辺の重みをmin_value以上max_value未満で指定します．

```
UndirectedGraph.gen_edges(n, m, min_value = 1, max_value = 10**9, is1index = False)
```

### 有向向グラフ(DirectedGraphクラス)

#### 共通の変数

$n$: 頂点の数, $m$: 辺の数  
is1index: trueで頂点番号を[1,n+1), falseで[0,n)で出力します．

#### 重みなしグラフの辺を作成する．

未作成

### 木構造(Treeクラス)

#### 共通の変数

$n$: 頂点の数, $root$: 根とする頂点(頂点番号は0indexで指定します)
is1index: trueで頂点番号を[1,n+1), falseで[0,n)で出力します．

#### 重みなしグラフの辺を作成する．

```
UndirectedGraph.gen_edges(n, root = 0, is1index = False)
```

#### 重みありグラフの辺を作成する．

辺の重みをmin_value以上max_value未満で指定します．

```
UndirectedGraph.gen_edges(n, root = 0, min_value = 1, max_value = 10**9, is1index = False)
```

### 文字列(Stringクラス)

#### 共通の変数
$lw$: アルファベットの小文字26文字  
$up$: アルファベットの大文字26文字

#### 決められたパターンから文字列を作成する

長さ$n$の文字列を作成します．各文字はchar_listの中からランダムに選ばれます．

```
String.gen_string(n, char_list = lw)
```
