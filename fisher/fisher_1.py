from flask import Flask
#from config import DEBUG#将配文件当做模块导入它。

__author__ = '七月'

#实例化Flask对象

app = Flask(__name__)
#APp核心对象提供的导入方法，载入配置文件
app.config.from_object('config')#模块路径。通过该方式导入的模块要求全部大写。不能有小写。


#装饰器可以解决代码耦合的问题，
#Flask实际上只做了一个重定向 ，浏览器访问url1的地址。然后给服务器。服务器返回loacation.并且给一个状态码。和一个值。301或者是302是重定向代码。
@app.route('/hello/')#通过装饰器给hello定义一个url，让其可以通过http去访问
def hello():#这个就是一个控制器，MVC模式里面的contral
    #Flask里面有一个基于类的视图（既插视图）
    return "hello"#定义视图。通过http请求访问函数

#如果要使用基于类的视图需要一定使用add_url_rule,Flask用了封装。把视图封装成了该装饰器
#app.add_url_rule('/hello/',view_func=hello) #用Flask的核心函数。注册路由。其指定视图函数为hello()




#入口文件的判断。具体的意义为flask。生产环境。服务器的
if __name__ == '__main__':
    #生产环境。前置服务器nginx。分配到uwsgi加载fisher模块启动代码。生产环境中fisher不是入口文件。所以必须加if判断。
    # 可以改端口改ip。将开发模式部署到生产环境中不能用debug调试模式。
    # 保证开发环境和生产环境中的源代码一定要是镜像关系。所以启用配置文件
    app.run(host="0.0.0.0", debug=app.config['DEBUG'],port=81)#打开Flask调试模式。让其改一次代码自动重启服务器

