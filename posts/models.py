from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    color = ColorField(format="hexa")

    def __str__(self):
        return self.title
    