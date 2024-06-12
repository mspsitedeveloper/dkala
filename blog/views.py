from django.views.generic import TemplateView , CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class Home(TemplateView):
    template_name = 'home.html'

class NewPost(CreateView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    model = Post