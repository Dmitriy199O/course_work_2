import json


def get_all_posts():
    with open('data.json', 'r', encoding='utf-8') as f:
        all_posts = json.load(f)
        return all_posts


def get_post_by_username(username):
    all_posts = get_all_posts()
    posts=[]

    for item in all_posts:
        if username.lower() == item['poster_name'].lower():
            item['comments']=get_comments_by_post_id(item['pk'])
            item['comments_count']=len(item['comments'])
            posts.append(item)
    return posts




def get_comments_by_post_id(post_id):
    with open('comments.json', 'r', encoding='utf-8') as f:
        all_comments = json.load(f)
        all_comments_by_id = []
        for item in all_comments:
            if post_id == item['post_id']:
                all_comments_by_id.append(item)
        return all_comments_by_id


def search_for_posts(key_word):
    all_posts = get_all_posts()
    posts_lists = []
    for post in all_posts:
        if key_word in post['content']:
            posts_lists.append(post)
    return posts_lists


def get_post_by_pk(pk):
    all_posts = get_all_posts()
    posts_list = []
    for post in all_posts:
        if pk == post['pk']:
            post['comments'] = get_comments_by_post_id(post['pk'])
            post['comments_count'] = len(post['comments'])
            posts_list.append(post)
    return posts_list


print(get_post_by_pk(1))
