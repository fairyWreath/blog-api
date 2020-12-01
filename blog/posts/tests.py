from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):

    @classmethod        # method bound to class not object of the class
    def setUpTestData(cls):         # set up data/objects for testing
        testuser1 = User.objects.create_user(       # django User model has username and pw
            username = 'testuser1',
            password = 'testuser1pw'    
        )

        test_post = Post.objects.create(author=testuser1, title='blog title', body='body content')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)       # in a testcase everything is 'renewed'
        author = f'{post.author}'   # f string formatting in python
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'blog title')
        self.assertEqual(body, 'body content')




