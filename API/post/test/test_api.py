from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Post
import pytest
import json


@pytest.mark.django_db
class TestBasePost(TestCase):

    def setUp(self):
        self.client = Client()
        self.post_url = reverse('post_list')
        self.user_1 = User.objects.create(username='mark')
        self.user_2 = User.objects.create(username='jasmine')


class TestGetPost(TestBasePost):

    def test_zero_post_should_return_empty_list(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['data'], [])
        self.assertEqual(json.loads(response.content)['count'], 0)

    def test_create_one_post_should_succed(self):
        data_test = {'title': 'the war in ukraine',
                     'content': 'the war between ukraine and russia',
                     'author': self.user_1,
                     'status': 'Politics'
                     }
        post_test = Post.objects.create(**data_test)
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)
                         ['data'][0]['title'], post_test.title)
        self.assertEqual(json.loads(response.content)
                         ['data'][0]['content'], post_test.content)
        self.assertEqual(json.loads(response.content)['count'], 1)


class TestCreatePost(TestBasePost):

    def test_create_post_without_title_should_fail(self):
        data_test = {'title': '',
                     'content': 'the war between ukraine and russia',
                     'author': self.user_1,
                     }
        response = self.client.post(self.post_url, data=data_test)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content),
                         {"title": ["This field may not be blank."]})

    def test_create_post_without_title_should_fail(self):
        data_test_1 = {'title': 'the war in ukraine',
                       'content': 'the war between ukraine and russia',
                       'author': self.user_1,
                       }
        data_test_2 = {'title': 'the war in ukraine',
                       'content': 'the war between ukraine and russia',
                       'author': self.user_2,
                       }
        Post.objects.create(**data_test_1)
        response = self.client.post(self.post_url, data=data_test_2)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content),
                         {"title": ['post with this title already exists.']})
