from flask import Flask, url_for

app = Flask(__name__)


@app.route('/promotion_image/<name>')
def promotion(name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Летим на: {name}</h1>
                    <div class="alert-dark" role="alert">
                      <br><h3>"Чебурек"</h3>
                    </div>
                    <div class="alert-success" role="alert">
                      <br><h3>"Планета Чебурек"</h3>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h3>"Торт"</h3>
                    </div>
                    <div class="alert-warning" role="alert">
                      <br><h3>"Планета Тортик"</h3>
                    </div>
                    <div class="alert-danger" role="alert">
                      <br><h3>"Пончик"</h3>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
