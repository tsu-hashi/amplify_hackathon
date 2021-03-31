# Bookshelf optimization
本ファイルはjupyter notebookで実装.

## 実行方法
1. jupyter notebookを起動し、bookshelf_optimization.ipynbファイルをアップロードする。
2. 1セル目のTOKENに適切なアクセストークンを設定する。
3. 1セル目のPROXYに適切なプロキシを設定する。不要であれば、
   FixstarsClient(proxy=PROXY)のproxyの部分を削除する。
4. [Cell] - [Run All]を実行する。

## 実行結果
最終セル（実行結果）を参照 

result : OK or NG
 * OK : 求解に成功した
 * NG : 求解に失敗した

result=OKの場合は、求解結果の可視化が行われる。
