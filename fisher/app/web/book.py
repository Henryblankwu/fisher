from flask import jsonify
#from fisher import app# 无法直接导入flask的核心对象app
# from flask import Blueprint#导入蓝图
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web

#应该创建视图蓝图。buleprint，将视图函数注册到蓝图对象上，由蓝图最终插入flask核心对象上，
# web = Blueprint('web' ,__name__)# 通常情况下用python 内置的__name__来代表蓝图所在的包。接受蓝图的参数。第一个web，第二个为蓝图所在的包

@web.route("/bool/search/")# 用web 来注册视图函数。API的设计难点就在于此，路由设计
def search():#接收q和page的参数。
    '''
    ？q=金庸&page=1，让q作为查询参数
    q,普通关键字和page isbn参数。需要编写代码来判断到底是调用的普通关键字还是isbn
    page
    s视图函数不能写太复杂太长的代码，方便后期阅读维护
    '''
    # app.add_url_rule('url',view_func=,endpoint= )
    # Request Response#(通过Request实例化对象来进行)
    # 几乎包含所有http请求信息
    # 查询参数 remote
    isbn_or_key = is_isbn_or_key(q)#这实际上就是一种封装
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)#pythonFlask自带返回json方法，可代替下面代码。
    # return json.dumps(result),200,{'content-type':'application/json'}