from flask import jsonify, request, current_app

from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook



@web.route('/book/search/<q>/<page>')
def search(q, page):
    """

    :param q: 普通关键字，isbn
    :param page:
    :return:
    """
    # alt+enter:导入模块
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    #return json.dumps(result), 200, {'content-type': 'application/json'}

@web.route('/')
def index():
    args_value  = request.args
    print(args_value)
    return 'hello'

@web.route('/test1')
def test1():
    print(id(current_app))
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-----------------')
    return ''
