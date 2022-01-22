from operator import truth
from flask import Flask,render_template
from data import Articles
import re
import os
from importlib import reload

app = Flask(__name__)

Articles = Articles()


@app.route("/")
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id =id)                


def get_port():
      return int(os.environ.get("PORT", 33507))

def create_app():
    app = Flask(__name__)
if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=get_port())
