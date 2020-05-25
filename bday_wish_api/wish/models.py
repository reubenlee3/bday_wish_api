from django.db import models

# Create your models here.
class Wish(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    wish = models.TextField()
    # image?

    def __str__(self):
        return self.author