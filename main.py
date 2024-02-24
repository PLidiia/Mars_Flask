from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марс'


@app.route('/promotion_image')
def do_image_mars():
    return f'''<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Колонизация</title>
    <link crossorigin="anonymous" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" rel="stylesheet">
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
<h1>Жди нас, Марс!</h1>
<img src="{url_for('static', filename='img/Mars.png')}" alt="Фото Марса">
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
        crossorigin="anonymous"></script>
<div class="alert alert-dark" role="alert">
  Человечество вырастает из детства.
</div>
<div class="alert alert-success" role="alert">
  Человечеству мала одна планета.
</div>
<div class="alert alert-secondary" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты.
</div>
<div class="alert alert-warning" role="alert">
  И начнем с Марса!
</div>
<div class="alert alert-danger" role="alert">
 Присоединяйся!
</div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
