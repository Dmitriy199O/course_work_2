from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)


@app.route('/posts/<postid>/')
def comments_by_id(postid):
    get_comms = get_comments_by_post_id()

    return render_template('post.html')


app.run(debug=True)
