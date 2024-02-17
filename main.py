from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def do_promo():
    with open('design.html', 'r', encoding='utf-8') as design_file:
        return design_file.read()


@app.route('/image_mars')
def do_image_mars():
    with open('image_mars_design.html', 'r', encoding='utf-8') as design_file:
        return design_file.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
