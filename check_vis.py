#H1のハード制約を満たすかチェックする
def check_h1(df_book, sample):
    result = True
    for j in range(shelf_y):
        book_len = sum(sum(sample("x" + "[" + str(i) + "]" + "[" + str(j) + "]" + "[" + str(k) + "]" ) * df_book["厚さ(mm)"][i] for i in range(book_num)) for k in range(shelf_x))
        if book_len > 3000:
            result = False
            break
    return result

#H2のハード制約を満たすかチェックする
def check_h2(sample):
    result = True
    for i in range(book_num):
        book_total = sum(sum(sample("x" + "[" + str(i) + "]" + "[" + str(j) + "]" + "[" + str(k) + "]" ) for j in range(shelf_y)) for k in range(shelf_x))
        if book_total > 1:
            result = False
            break
    return result

#収納できた本の冊数を表す
import itertools
def total(sample):
    pro = itertools.product(range(book_num), range(shelf_y), range(shelf_x))
    total = sum(sample("x" + "[" + str(i) + "]" + "[" + str(j) + "]" + "[" + str(k) + "]") for i, j, k in pro)
    
#収納を可視化する
import pandas as pd
def vis(sample, df_book):
    pro = itertools.product(range(book_num), range(shelf_y), range(shelf_x))
    _df = pd.DataFrame([[i, j, k, sample("x" + "[" + str(i) + "]" + "[" + str(j) + "]" + "[" + str(k) + "]")] for i, j, k in pro])
    _df = _df.rename(columns={0:'index', 1:'上から何段目', 2:'左から何冊目', 3:"存在"})
    _df = _df[_df["存在"] == 1]
    df = pd.merge(_df, df_book, on="index", how="left")
    df = df.drop('存在', axis=1)
    return df

#ソフト制約はペナルティが不明のため未製作