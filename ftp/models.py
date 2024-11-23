from django.db import models
from . stroge_backends import FtpStorage


# Create your models here.
class Ftp(models.Model):
    image = models.ImageField(upload_to='', storage=FtpStorage())
    