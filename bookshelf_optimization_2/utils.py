
def rename_df_book(df_book):
    rename_dict = {
        'タイトル': 'title',
        'シリーズ': 'series',
        '厚さ(mm)': 'width',
        '高さ(mm)': 'height',
        '著者名': 'author',
        '背表紙の色':'color_name',
        '色番号': 'color',
        '使う頻度': 'freq',
        'ジャンル': 'genre',
    }
    df_book = df_book.rename(columns=rename_dict)
    return df_book


def calc_max_books_per_shelf(df_book, shelf_width):
    # sort by width
    tmp_df = df_book.sort_values(['width'])
    # calc cummulative width
    tmp_df['cum_width'] = tmp_df['width'].cumsum()
    # calc maximum number of books per one shelf
    max_books_per_shelf = tmp_df[tmp_df['cum_width'] <= shelf_width].shape[0]
    return max_books_per_shelf


def binary_expr(n, max_coef=None):
    i = 0
    indices = []
    while (n - 2 ** i) > 0:
        indices.append(2 ** i)
        n -= 2 ** i
        if (max_coef is None) or (max_coef >= (2 ** (i+1))):
            i += 1
        else:
            pass

    if n == 0:
        pass
    else:
        indices.append(n)
    return indices