from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Post
import pytest
import json


@pytest.mark.django_db
class TestGetPost(TestCase):

    def test_zero_post_should_return_empty_list(self):
        client = Client()
        post_url = reverse('post_list')
        response = client.get(post_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['data'], [])
        self.assertEqual(json.loads(response.content)['count'], 0)

    def test_create_one_post_should_succed(self):
        user = User.objects.create(username='mark')
        data_test = {'title': 'the war in ukraine',
                     'content': 'the war between ukraine and russia',
                     'author': user,
                     'status': 'Politics'
                     }
        post_test = Post.objects.create(**data_test)
        client = Client()
        post_url = reverse('post_list')
        response = client.get(post_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)
                         ['data'][0]['title'], post_test.title)
        self.assertEqual(json.loads(response.content)
                         ['data'][0]['content'], post_test.content)
        self.assertEqual(json.loads(response.content)['count'], 1)
