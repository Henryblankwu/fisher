#初始化核心对象
from flask import Flask



def create_app():
    # 入口文件只做初始化和项目启动。
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(app)# 在此调用
    return app

#创建一个函数专门用于注册蓝图。
def register_blueprint(app):
    from app.web.book import web # 由于临时导入需要。所以可以再内部使用from
    app.register_blueprint()#使用app的方法来注册蓝图