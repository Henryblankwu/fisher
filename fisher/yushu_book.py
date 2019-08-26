from http import HTTP

class YuShuBook:#由于有2种搜索方式所以定义2种搜索类

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'#isbn的API,关键变量在{}里面。会动态传
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'#关键字的API

    @classmethod#由于self没有用到该参数。所以改为cls.修饰符。直接调用类的属性，类的方法。
    def search_by_isbn(cls,isbn):#将isbn号作为参数传入
        url = cls.isbn_url.format(isbn)#格式化得到完整url，除了用YuShuBook.isbn_url之外还可以用链式查找。self.isbn_url进行查找读取。
        result = HTTP.get(url)#用http去接受
        #由于ISBN是json格式。所以result会直接返回一个字典。
        return result

    def search_by_keyword(cls,self,count=15,start=0):
        url = cls.isbn_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result