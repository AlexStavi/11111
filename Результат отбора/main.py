from flask import Flask, url_for

app = Flask(__name__)


@app.route('/results/<name>/<int:level>/<float:rating>')
def results(name, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претедента на участие {name}</h3>
                    <div class="alert-success" role="alert">
                      <br><h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                    </div>
                    <div class="txtResult">
                       <h3>Составляет {rating}</h3>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h3>"Желаем удачи"</h3>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
