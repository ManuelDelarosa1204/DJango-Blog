from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path(
        "profile/<slug:slug>/create-post/",
        views.CreatePost.as_view(),
        name="create_post",
    ),
    path("profile/<str:username>/<slug:slug>/", views.ReadPost.as_view(), name="post"),
]
