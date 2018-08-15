#  flask如何启动 WEB 服务器？
# 导入Flask类
from flask import Flask
# Flask函数接收一个参数__name__，它会指向程序所在的包

app = Flask(__name__,  # 这里可以写错，不要写abc
            static_url_path='/static', # 访问静态文件的url前缀
            static_folder='static',
            template_folder='templates' #
            )

# 调试模式：第一种
#class Config(object):
    #"""
    #配置类，将配置信息通过属性方式罗列
    #:return None
    #"""
    # DEBUG = True
# 配置文件
# app.config.from_object(Config)

# 第二种
# app.config.from_pyfile("config.ini")

# 第三种
# app.config.from_envvar("flask_config")

#  常用的配置也会在app中保留一份
# app.debug = True
app.config["DEBUG"] = True

# 根路由
# 装饰器的作用是将路由映射到视图函数 index
@app.route('/')
def index():
    print(app.url_map)

    """
    Map([<Rule '/' (OPTIONS, GET, HEAD) -> index>,
    <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])
    # url_map 将装饰器路由和视图的对应关系保存起来
    """

    """
    除0的错误
    以上有三种debug的方法
    """
    # a = 1/0
    return '你好啊，第一个路由器'


if __name__ == '__main__':
    # app.run()  # Flask应用程序实例的 run 方法 启动 WEB 服务器
    app.run(host="10.211.55.11", port=8888)