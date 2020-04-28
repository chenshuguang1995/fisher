from flask import jsonify

from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook


print('id为' + str(id(app)) + '的app注册路由')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q普通关键字 isbn  isbn13:13位数字   isbn10:0到9,中间包含'-'
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type' : 'application/json'}
    return jsonify(result)