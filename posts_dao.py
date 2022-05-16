import json


class PostsDao:

    def get_all_posts(self):

        """
        Открываем файл и получаем из него данные
        :return:   list
        """

        with open('data.json', 'r', encoding='utf-8') as f:
            all_posts = json.load(f)
            return all_posts

    def get_post_by_username(self, username):

        """
        Получаем список постов по имени пользователя
        :param username:
        :return: list
        """

        all_posts = self.get_all_posts()
        posts = []

        for item in all_posts:
            if username.lower() == item['poster_name'].lower():
                item['comments'] = self.get_comments_by_post_id(item['pk'])
                item['comments_count'] = len(item['comments'])
                posts.append(item)
        return posts

    def get_comments_by_post_id(self, post_id):

        """
        Получаем список комментов по идентификатору
        :param post_id:
        :return: list
        """

        with open('comments.json', 'r', encoding='utf-8') as f:
            all_comments = json.load(f)
            all_comments_by_id = []
            for item in all_comments:
                if post_id == item['post_id']:
                    all_comments_by_id.append(item)
            return all_comments_by_id

    def search_for_posts(self, key_word):

        """
        Ищем посты ,содержащие ключевое слово
        :param key_word:
        :return: list
        """

        all_posts = self.get_all_posts()
        posts_lists = []
        for post in all_posts:
            if key_word in post['content']:
                posts_lists.append(post)
        return posts_lists

    def get_post_by_pk(self, pk):

        """
        Получаем посты по идентификатору
        :param pk:
        :return: list
        """

        all_posts = self.get_all_posts()
        posts_list = []
        for post in all_posts:
            if pk == post['pk']:
                post['comments'] = self.get_comments_by_post_id(post['pk'])
                post['comments_count'] = len(post['comments'])
                posts_list.append(post)
        return posts_list

dao=PostsDao()
print(dao.get_post_by_pk(2)[0])