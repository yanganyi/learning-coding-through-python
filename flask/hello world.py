from flask import Flask

app = Flask('main')


@app.route('/')
def hello_world():
    return '<b><a href="http://www.google.com">Hello, world!</a></b>'


app.run()
