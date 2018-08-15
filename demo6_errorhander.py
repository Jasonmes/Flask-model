from flask import Flask, abort, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 主动产生一个404的错误
    # 参数1：必须是http的错误状态码
    abort(404)
    return "Hello World!"


@app.errorhandler(404)
def error1(error):
    print(error)
    # 捕获404异常，然后重定向到百度官网
    return redirect("https://www.baidu.com")

if __name__ == '__main__':
    app.run(debug=True)