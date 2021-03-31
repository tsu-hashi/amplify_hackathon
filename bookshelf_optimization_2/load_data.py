import pandas as pd
import numpy as np
from itertools import product

DATA_DIR = './data'

def load_book_author():
    # 苗字ランキング上位40と新生児の名前ランキング上位40位で組み合わせは1600種類
    df_name = pd.read_csv(f"{DATA_DIR}/name.csv")
    df_name = pd.DataFrame(list(product(df_name['苗字'], df_name['名前'])), columns=['苗字', '名前'])
    df_name["氏名"] = df_name["苗字"] + df_name["名前"]
    df_name = df_name["氏名"]
    return df_name


def load_book_size():
    df_size = pd.read_csv(f"{DATA_DIR}/book_size.csv")
    return df_size


def load_book_color():
    df_color = pd.read_csv(f"{DATA_DIR}/color.csv")["色"]
    return df_color


def make_bookdata(num_books, df_size, df_name, df_color):
    np.random.seed(0)
    series_id = 0
    df_book = pd.DataFrame(columns=['タイトル', 'シリーズ', '厚さ(mm)', '高さ(mm)', '著者名', '背表紙の色', '色番号', '使う頻度'])
    while num_books:
        num_series = max(int(np.random.rand() * np.random.rand()//0.1), 1)
        if num_books < num_series:
            num_series = num_books
            num_books = 0
        else:
            num_books -= num_series
        df_tmp = pd.DataFrame([[f"{series_id}_{i}",series_id] for i in range(num_series)], columns=['タイトル', 'シリーズ'])

        df_tmp['厚さ(mm)'] = np.random.randint(30, 41)
        df_tmp['高さ(mm)'] = df_size['高さ'][np.random.randint(len(df_size))]
        df_tmp['著者名'] = df_name[np.random.randint(len(df_name))]

        for i in range(num_series):
            color_num = np.random.randint(len(df_size))
            df_tmp.at[i,'背表紙の色'] = df_color[color_num]
            df_tmp.at[i,'色番号'] = color_num
            df_tmp.at[i,'使う頻度'] = np.random.randint(10)
        df_book = pd.concat([df_book, df_tmp]).reset_index(drop=True)
        series_id += 1

    return df_book


def load_book_data(n_books=1000, refresh=True):
    if refresh:
        df_name  = load_book_author()
        df_size  = load_book_size()
        df_color = load_book_color()
        df_book  = make_bookdata(n_books, df_size, df_name, df_color)
    else:
        df_book = pd.read_csv("../../books.csv", index_col=0)
        df_book = df_book[:n_books]

    return df_book

