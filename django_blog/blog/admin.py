from django.contrib import admin
from .models import Post


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
