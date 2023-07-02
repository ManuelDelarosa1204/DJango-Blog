from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from user.models import User


class TestReadPostView(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='johndoe123',
            slug='johndoe123'
        )

        self.post = Post.objects.create(
            title='Test Post',
            body='This is a test post',
            slug='test-post',
            author=self.user
        )

    def test_url_exists_at_location(self):
        response = self.client.get(
            f'/profile/{self.post.author.username}/{self.post.slug}/'
        )
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse('blog:post', args=[
                    self.post.author.username, self.post.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(
            reverse(
                'blog:post', args=[self.post.author.username, self.post.slug]
            )
        )
        self.assertTemplateUsed(response, 'blog/read-post.html')

    def test_template_contains_correct_data(self):
        response = self.client.get(
            reverse(
                'blog:post', args=[self.post.author.username, self.post.slug]
            )
        )
        self.assertContains(response, self.post.title, html=True)


class TestCreatePostView(TestCase):
    def test_url_exists_at_location(self):
        response = self.client.get(
            f'/profile/johndoe123/create-post/'
        )
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse(
                'blog:create_post', args=['johndoe123']
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(
            reverse(
                'blog:create_post', args=['johndoe123']
            )
        )
        self.assertTemplateUsed(response, 'blog/create-post.html')

    def test_template_has_correct_form(self):
        response = self.client.get(
            reverse(
                'blog:create_post', args=['johndoe123']
            )
        )

        # Check that the label for the title
        # field is present in the template
        self.assertContains(
            response,
            '<label for="id_title">Title:</label>',
            html=True
        )
