import json

from flask import Flask, jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
print('id为' + str(id(app)) + '的app实例化')
app.config.from_object('config')

# 这种方式导入flask默认必须大写
# print(app.config['DEBUG'])


@app.route('/hello')
def hello():
    return 'Hello Chen'


from app.web import book


if __name__ == '__main__':
    print('id为' + str(id(app)) + '的app启动')
    # 生产环境 Nginx+uwsgi部署,不加会产生两个web服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
