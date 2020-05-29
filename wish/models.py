from django.db import models
from PIL import Image

# Create your models here.
class Wish(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    wish = models.TextField()
    image = models.ImageField(default='default.png')

    def __str__(self):
        return self.author