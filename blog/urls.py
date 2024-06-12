from django.urls import path
from .views import Home , NewPost
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/new', NewPost.as_view(), name='new_post'),
]