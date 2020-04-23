from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
# 这种方式导入flask默认必须大写
print(app.config['DEBUG'])


@app.route('/hello')
def hello():
    return 'Hello Chen'


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q普通关键字 isbn  isbn13:13位数字   isbn10:0到9,中间包含'-'
        page
    """
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit:
        isbn_or_key = 'isbn'
    pass


if __name__ == '__main__':
    # 生产环境 Nginx+uwsgi部署,不加会产生两个web服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
