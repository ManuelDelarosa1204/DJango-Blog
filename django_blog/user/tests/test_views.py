from django.test import TestCase
from django.urls import reverse
from user.models import User


class TestUserProfilePage(TestCase):
    """Tests to be ran for the user profile view"""

    def setUp(self):
        """Create a user to be used for some of the views"""
        self.user = User.objects.create(
            first_name='john',
            last_name='doe',
            username='johndoe123',
            email='johnd@site.com',
            slug='johndoe123',
        )

    def test_url_exists_at_location(self):
        """Make sure the url is at the desired location"""
        response = self.client.get(f'/profile/{self.user.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse('user:profile', args=[self.user.slug]))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(
            reverse('user:profile', args=[self.user.slug]))
        self.assertTemplateUsed(response, 'user/profile.html')

    def test_template_has_correct_user(self):
        response = self.client.get(
            reverse('user:profile', args=[self.user.slug]))
        self.assertContains(response, self.user.username, html=True)
