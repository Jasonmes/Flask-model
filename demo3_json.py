from flask import Flask, jsonify
# import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    # 定义字典
    dict = {
        "name":"james",
        "age":33,
        "info":{
            "team":"laker"
        }
    }
    # 将python字典转换成json字符串
    # json_str = json.dumps(dict)
    # 将json字符串转换成python字典类型
    # my_dict = json.loads(json_str)

    # 使用jsonify也可以转换
    """
    1. 能够将python字典转化成json文件
    2. 能帮助我们指定返回的类型的对象
    3. 将数据包装成response响应对象
    """
    json_str1 = jsonify(dict)
    return json_str1


if __name__ == '__main__':
    app.run(debug=True)