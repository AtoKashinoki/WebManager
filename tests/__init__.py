

import flask


app = flask.Flask(__name__)

@app.route("/")
def index():
    return "<a href='/test'>test</a>"

@app.route("/test")
def test():
    return "<a href='/'>return</a>"


if __name__ == '__main__':
    app.run()
    ...
