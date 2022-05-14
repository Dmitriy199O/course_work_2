from flask import Flask, render_template, request, jsonify
from posts_dao import PostsDao

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
posts_dao = PostsDao()


@app.route('/')
def main_page():
    posts = posts_dao.get_all_posts()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_pk>/')
def post_page(post_pk):
    post = posts_dao.get_post_by_pk(post_pk)
    comments = posts_dao.get_comments_by_post_id(post_pk)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search/')
def search_page():
    search_by = request.args.get('s')
    posts = posts_dao.search_for_posts(search_by)
    return render_template('search.html', posts=posts, search_by=search_by)


@app.route('/users/<username>/')
def user_page(username):
    post = posts_dao.get_post_by_username(username)
    return render_template('user-feed.html', post=post)


@app.route('/api/posts/', methods=['GET'])
def posts_json():
    posts = posts_dao.get_all_posts()
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>/', methods=['GET'])
def post_json(post_id):
    post = posts_dao.get_post_by_pk(post_id)
    return jsonify(post)

if __name__=="__main__":

    app.run(debug=True)
