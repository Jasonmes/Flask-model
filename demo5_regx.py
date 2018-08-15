from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 自定义转换器
class RegexConverter(BaseConverter):
    # 重写父类的regx属性，将自定义的正则复制给他
    # regex = "[0-9]{6}"
    def __init__(self, url_map, re):
        super(RegexConverter, self).__init__(url_map)
        self.regex = re

# 将自定义好的类，注册到url_map.converters这个字典中
app.url_map.converters['re'] = RegexConverter


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/user/<re("[0-9]{6}"):user_id>')
def demo1(user_id):
    return "demo1 %s" % user_id


if __name__ == '__main__':
    app.run(debug=True)