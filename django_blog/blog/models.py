from django.db import models
from user.models import User
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    """Model to deal with all post"""
    class Status(models.TextChoices):
        """Class to use for post statuses"""
        PUBLIC = 'PUBLIC', 'Public'
        DRAFT = 'DRAFT', 'Draft'

    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    # Date and time the post was created
    posted_date = models.DateTimeField(default=timezone.now)
    # Date and time of the last time the post
    # was updated, if the post has been updated
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    # Give user the choice to either have their
    # post be public or saved as a draft
    status = models.CharField(
        max_length=6, choices=Status.choices, default=Status.PUBLIC)

    def save(self, *args, **kwargs) -> None:
        """Set the value of the slugfield to be the same value as the title"""
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        # Order be `posted date` descending
        ordering = ['-posted_date']

        # Create index for query optimization
        indexes = [
            models.Index(fields=['-posted_date'])
        ]
