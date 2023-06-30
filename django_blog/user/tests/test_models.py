from django.test import TestCase
from user.models import User


class TestUserModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='John',
            last_name='Doe',
            username='johndoe123',
            email='johnd@site.com',
        )

    def get_model_field(self, field: str):
        """Returns the `label` of a model field"""
        return self.user._meta.get_field(field).verbose_name

    def test_get_absolute_url(self):
        self.assertEqual(self.user.get_absolute_url(), '/profile/johndoe123/')

    def test_first_name_label(self):
        self.assertEqual(self.get_model_field('first_name'), 'first name')

    def test_last_name_label(self):
        self.assertEqual(self.get_model_field('last_name'), 'last name')

    def test_username_label(self):
        self.assertEqual(self.get_model_field('username'), 'username')

    def test_email_label(self):
        self.assertEqual(self.get_model_field('email'), 'email address')

    def test_password_label(self):
        self.assertEqual(self.get_model_field('password'), 'password')
