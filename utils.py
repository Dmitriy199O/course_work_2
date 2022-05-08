import json


def get_all_posts():
    with open('data.json', 'r', encoding='utf-8') as f:
        all_posts = json.load(f)
        return all_posts


def get_post_by_username(username):
    all_posts=get_all_posts()
    for item in all_posts:
        if username.lower() in item['poster_name']:
            return item['poster_name'],item['poster_avatar'],item['pic'],item['content'],item['pk']
    else:
        return f'There is no user named {username}'


def get_comments_by_post_id(post_id):
    with open('comments.json', 'r', encoding='utf-8') as f:
        all_comments = json.load(f)
        all_comments_by_id = []
        for item in all_comments:
            if post_id == item['post_id']:
                all_comments_by_id.append(item)
        return all_comments_by_id


def search_for_posts(key_word):
    all_posts=get_all_posts()
    posts_lists=[]
    for post in all_posts:
        if key_word.lower() in post['content'].lower():
            posts_lists.append(post)
    return posts_lists



def get_post_by_pk(pk):
    all_posts=get_all_posts()
    posts_list=[]
    for post in all_posts:
        if pk == post['pk']:
            posts_list.append(post)
    return posts_list



