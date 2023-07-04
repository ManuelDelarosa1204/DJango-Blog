from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'slug',
        'posted_date',
        'updated_date',
        'status',
    ]

    list_filter = [
        'status',
        'posted_date',
        'author',
    ]

    search_fields = [
        'title',
        'body',
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }

    date_hierarchy = 'posted_date'

    ordering = [
        'status',
        'posted_date',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'comment',
        'post',
        'author',
        'date_created',
    ]

    list_filter = [
        'post',
        'author',
        'date_created',
    ]

    search_fields = [
        'post',
        'author',
    ]

    date_hierarchy = 'date_created'

    ordering = [
        'date_created'
    ]
