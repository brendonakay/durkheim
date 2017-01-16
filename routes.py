from flask import Flask
from flask import render_template

app = Flask(__name__)

navigation = [
    {
    'href': '/',
    'caption': 'home'
    },

    {
    'href': '/page',
    'caption': 'page'
    }
]


@app.route('/')
def hello(name=None):
    return render_template('index.html', navigation=navigation)


@app.route('/page')
def hello(name=None):
    return render_template('page.html', navigation=navigation)