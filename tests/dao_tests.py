import pytest

from posts_dao import PostsDao

dao = PostsDao()

import app


class TestPostsDao:

    def test_get_all_posts(self):
        dao_all = dao.get_all_posts()
        assert isinstance(dao_all, list) == True
        assert isinstance(dao_all[0], dict) == True

    def test_get_post_by_username(self, username='hank'):
        dao.get_post_by_username(username)
        assert isinstance(dao.get_post_by_username(username), list) == True
        assert isinstance(dao.get_post_by_username(username)[0], dict) == True

    def test_get_comments_by_post_id(self, uid='2'):
        dao.get_comments_by_post_id(uid)
        assert isinstance(dao.get_comments_by_post_id(uid), list) == True
        assert isinstance(dao.get_comments_by_post_id(uid)[0], dict) == True

    def test_search_for_posts(self, keyword='кот'):
        dao.search_for_posts(keyword)
        assert isinstance(dao.search_for_posts(keyword), list) == True

    def test_get_post_by_pk(sel, pk='2'):
        dao.get_post_by_pk(pk)
        assert isinstance(dao.get_post_by_pk(pk), list) == True


class TestAPI:
    def test_api_get_all_posts(self):
        response = app.app.test_client().get('/api/posts/')
        assert response.status_code == 200

    def test_api_get_one_posts(self):
        response = app.app.test_client().get('/api/posts/1')
        assert response.status_code == 200
