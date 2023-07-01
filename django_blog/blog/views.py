from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostCreationForm
from user.models import User


class CreatePost(CreateView):
    """View to create post"""
    model = Post
    template_name = 'blog/create-post.html'
    form_class = PostCreationForm

    def get_success_url(self) -> str:
        return reverse_lazy('user:profile', args=[self.request.user.slug])

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReadPost(DetailView):
    model = Post
    template_name = 'blog/read-post.html'
    context_object_name = 'post'
