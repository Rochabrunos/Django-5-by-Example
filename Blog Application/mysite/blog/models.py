from django.db import models
from django.db.models.functions import Now

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(db_default=Now)
    # auto_now_add saves the date automatically when creating an object (tracks creation time)
    created = models.DateTimeField(auto_now_add=True)
    # auto_now will automatically update the date when saving an object (tracks last modification time)
    updated = models.DateTimeField(auto_now=True)

    # Django uses this method to return a string with the human-readable representation of the object
    def __str__(self):
        return self.title