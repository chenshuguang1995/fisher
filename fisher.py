import json

from app import create_app

# print('id为' + str(id(app)) + '的app实例化')
# 这种方式导入flask默认必须大写
# print(app.config['DEBUG'])

app = create_app()


if __name__ == '__main__':
    print('id为' + str(id(app)) + '的app启动')
    # 生产环境 Nginx+uwsgi部署,不加会产生两个web服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
