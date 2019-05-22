from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Upload(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(null = True, blank=True , max_length=100)
    caption = models.TextField(null = True, blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('upload')

