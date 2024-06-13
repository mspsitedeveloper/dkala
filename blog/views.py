from django.views.generic import DetailView , CreateView , ListView
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class Home(ListView):
    model = Post
    template_name = 'blog.html'

class Single(DetailView):
    model = Post
    template_name = 'single.html'

class NewPost(CreateView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    model = Post

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'abstract', 'body', 'photo']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')