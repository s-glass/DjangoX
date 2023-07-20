from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# title, owner, description

class Song(models.Model):
    title = models.CharField(max_length=64)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='song description or info')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', args=[str(self.id)])