from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse


class User(AbstractUser):
    """Model to be used for all users"""
    slug = models.SlugField()

    def save(self, *args, **kwargs) -> None:
        """
        Set the slug field to be the same
        as the username field.
        """
        self.slug = slugify(self.username)
        return super(User, self).save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        """
        Directs to user profile.

        Ex: /profile/johndoe/
        """
        return reverse('user:profile', args=[self.slug])

    def __str__(self) -> str:
        return self.username
