import pytest

from posts_dao import PostsDao

dao = PostsDao()

import app


class TestPostsDao:

    def test_get_all_posts(self):
        """
        Проверяем ,что метод возвращает список словарей

        """

        dao.get_all_posts()
        assert isinstance(dao.get_all_posts(), list) == True, 'not list'
        assert isinstance(dao.get_all_posts()[0], dict) == True, 'not dict'
        assert dao.get_all_posts()[0]['poster_name']
        assert dao.get_all_posts()[0]['poster_avatar']
        assert dao.get_all_posts()[0]['pic']
        assert dao.get_all_posts()[0]['content']
        assert dao.get_all_posts()[0]['views_count']
        assert dao.get_all_posts()[0]['likes_count']
        assert dao.get_all_posts()[0]['pk']

    def test_get_post_by_username(self, username='hank'):
        """
         Проверяем ,что метод возвращает список словарей, которые содержат нужные ключи
        :param username:

        """

        dao.get_post_by_username(username)
        assert isinstance(dao.get_post_by_username(username), list) == True, 'not list'
        assert isinstance(dao.get_post_by_username(username)[0], dict) == True, 'not dict'
        assert dao.get_post_by_username(username)[0]['poster_name']
        assert dao.get_post_by_username(username)[0]['poster_avatar']
        assert dao.get_post_by_username(username)[0]['pic']
        assert dao.get_post_by_username(username)[0]['content']
        assert dao.get_post_by_username(username)[0]['views_count']
        assert dao.get_post_by_username(username)[0]['likes_count']
        assert dao.get_post_by_username(username)[0]['pk']
        assert dao.get_post_by_username(username)[0]['comments']
        assert dao.get_post_by_username(username)[0]['comments_count']

    def test_get_comments_by_post_id(self, uid='1'):
        """
         Проверяем ,что метод возвращает список словарей
        :param uid:

        """

        dao.get_comments_by_post_id(uid)
        assert isinstance(dao.get_comments_by_post_id(uid), list) == True, 'not list'
        assert isinstance(dao.get_comments_by_post_id(uid)[0], dict) == True, 'not dict'
        assert dao.get_comments_by_post_id(uid)[0]['post_id']
        assert dao.get_comments_by_post_id(uid)[0]['commenter_name']
        assert dao.get_comments_by_post_id(uid)[0]['comment']
        assert dao.get_comments_by_post_id(uid)[0]['pk']

    def test_search_for_posts(self, keyword='кот'):
        dao.search_for_posts(keyword)
        assert isinstance(dao.search_for_posts(keyword), list) == True, 'not list'
        assert isinstance(dao.search_for_posts(keyword)[0], dict) == True, 'not dict'

        assert dao.search_for_posts(keyword)[0]['poster_name']
        assert dao.search_for_posts(keyword)[0]['poster_avatar']
        assert dao.search_for_posts(keyword)[0]['pic']
        assert dao.search_for_posts(keyword)[0]['content']
        assert dao.search_for_posts(keyword)[0]['views_count']
        assert dao.search_for_posts(keyword)[0]['likes_count']

    def test_get_post_by_pk(sel, pk='2'):
        dao.get_post_by_pk(pk)
        assert isinstance(dao.get_post_by_pk(pk), list) == True, 'not list'
        assert isinstance(dao.get_post_by_pk(pk)[0], dict) == True, 'not dict'
        assert dao.get_post_by_pk(pk)[0]['poster_name']
        assert dao.get_post_by_pk(pk)[0]['poster_avatar']
        assert dao.get_post_by_pk(pk)[0]['pic']
        assert dao.get_post_by_pk(pk)[0]['content']
        assert dao.get_post_by_pk(pk)[0]['views_count']
        assert dao.get_post_by_pk(pk)[0]['likes_count']


class TestAPI:
    def test_api_get_all_posts(self):
        """
        Проверяем сатус представления

        """

        response = app.app.test_client().get('/api/posts/')
        assert response.status_code == 200

    def test_api_get_all_posts_list(self):
        response = app.app.test_client().get('/api/posts/')
        assert type(response.json) == list, f'{response} is not list'

    def test_api_get_all_posts_valid_keys(self):
        valid_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

        response = app.app.test_client().get('/api/posts/')
        list_posts = response.json
        assert len(list_posts) > 0, 'empty json'
        for post in list_posts:
            post_keys = set(post.keys())
            assert post_keys == valid_keys, f'Keys {post_keys} are not in valid keys'
            assert post['pic'] != None, 'there is  no pic'

    def test_api_get_one_post(self):
        """
        Проверяем статус представления

        """

        response = app.app.test_client().get('/api/posts/1/')
        assert response.status_code == 200

    def test_api_get_one_post_is_dict(self):
        response = app.app.test_client().get('/api/posts/1/')
        assert type(response.json) == list, f' {response} is not list'

    def test_api_get_one_post_valid_keys(self):
        valid_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        response = app.app.test_client().get('/api/posts/1/')
        post_keys = response.json.keys()
        post_dict = response.json
        assert post_keys == valid_keys, f' {post_keys} are not in valid keys'
        assert post_dict['pic'] != None, 'there is  no pic'
