from django.db import models
from datetime import date
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
    photo = models.ImageField(upload_to='photo/%y/%m/%d')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("single", kwargs={'pk': self.pk })