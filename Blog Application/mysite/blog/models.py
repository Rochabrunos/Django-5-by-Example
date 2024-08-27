from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    # Django uses this method to return a string with the human-readable representation of the object
    def __str__(self):
        return self.title