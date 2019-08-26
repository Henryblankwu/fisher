

def is_isbn_or_key(word):#传入word参数
    # isbn13.由13个0-9的数字组成
    # isbn10,由10个0-9的数字组成，其中含有'-'
    # 以下代码是判断搜索的。需要重构成函数。然后让视图调用
    isbn_or_key = 'key'  # 让其默认接受为key
    if len(word) == 13 and word.isdigit():  # 判断q是否全是13位数字。
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')  # 定义一个把-简化成空格的q
    if '-' in word and len(short_word) == 10 and short_word.isdigit:  # 该判断有效率先后之分。先把容易判断成假的放在前面。然后判断后面的提高效率
        isbn_or_key = 'isbn'
    #返回函数遍历
    return isbn_or_key
