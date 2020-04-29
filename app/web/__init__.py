# from flask import Blueprint

# from app.web import book

# web = Blueprint('web', __name__)

# 引入book模块,代码执行才会注册路由,不引入的话book文件没有被执行,注册不成功.
from app.web import book