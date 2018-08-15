from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    """
    自定义状态码
    返回的形式是一个元祖
    :return:
    """
    return "反向函数在调用index", 666


@app.route("/demo1")
def demo():
    # 重定向到黑马官网
    # 参数：重定向网页即可
    return redirect("http://www.itheima.com")

@app.route('/demo2')
def demo2():
    # 重定向自己的主页
    # url_for 反向解析函数
    # 作用url_for(函数名称)根据函数名称获取到这个视图函数对应的url
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)