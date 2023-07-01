from django.test import TestCase
from blog.models import Post
from user.models import User
from utils.models import get_model_field_label


class TestPostModel(TestCase):
    def setUp(self):
        self.author = User.objects.create(
            first_name='John',
            last_name='Doe',
            username='johndoe123',
            slug='johndoe123',
            email='johnd@site.com',
        )

        self.post = Post(
            title='First Post',
            body='This is my first post',
            slug='first-post',
        )

    # Test to make sure all the labels (verbose name) for
    # the model fields are correct

    def test_post_title_label(self):
        self.assertEqual(get_model_field_label(Post, 'title'), 'title')

    def test_post_body_label(self):
        self.assertEqual(get_model_field_label(Post, 'body'), 'body')

    def test_post_status_label(self):
        self.assertEqual(get_model_field_label(Post, 'status'), 'status')
