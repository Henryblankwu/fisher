from flask import Blueprint

web = Blueprint('web',__name__)

#视图函数的模块全部导入到init里面。实现视图函数注册
from app.web import book
from app.web import user