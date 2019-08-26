#将http请求封装到这个模块里
from urllib import request
import requests
class HTTP:
    #python2和python3中分经典类和新式类。所以在http后面传参（object)与否是有差别的
    #urllib python自带的库发送htttp请求
    #requests 第三方库发送
    @staticmethod#git为静态方法
    def get(self,url,return_json=True):#添加2个参数。一个为默认情况下请求的url，另一个为返回请求的json
        #r为对这次requests请求的封装。
        r = requests.get(url)#2个API均为git请求。所以用git
        # restful 大多数提供的API都是restful。比如github
        # json
        #下面代码的简写.三元表达式简化写法。一个函数建议只有一个return.而不是多个.但是应对复杂编程的时候。多个retuan.是优于单个。能减少开发难度。
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # if r.status_code == 200:#根据状态码来进行判断。200则是能找到isbn数据。400则找不到
        #     if return_json:
        #         return r.json()#返回json格式的字符串
        #     else:
        #         return r.text()#返回普通字符串对象
        # else:
        #     if return_json(): #跟上面保持一致写法
        #         return {}#找不到状态码不为200则返回400，返回空字典
        #     else:
        #         return ''#返回空字符串