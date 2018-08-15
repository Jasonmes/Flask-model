from flask import Flask

app = Flask(__name__)

# 127.0.0.1:5000/demo1 ---> demo1  视图函数
@app.route("/demo1")
def demo1():
    return "正在自定义路由路径"


# 127.0.0.1:5000/user/1 ---> demo2  视图函数
# 如何拿到末尾的1这个参数,这个参数默认是str类型
# 想改变参数类型 <int:user_id>
@app.route("/user/<user_id>")
def demo2(user_id):
    return "demo2 %s" % user_id

# 修改访问方式
# 通过methods列表属性修改视图函数的请求方式
@app.route("/demo3", methods=['POST'])
def demo3():
    return "demo3"


if __name__ == '__main__':
    app.run(debug=True)