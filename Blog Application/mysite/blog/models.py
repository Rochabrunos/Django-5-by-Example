from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) # Implies an index by default
    # Defines a many-to-one relationship between Users and Posts
    author = models.ForeignKey( # Implies an index by default
        settings.AUTH_USER_MODEL, # Points to auth.User by default
        on_delete=models.CASCADE,
        null=True,
        related_name='blog_posts', # specify the name of the reverse relationship, e.g. user.blog_posts
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # Has an index specifies in the Meta class
    # auto_now_add saves the date automatically when creating an object (tracks creation time)
    created = models.DateTimeField(auto_now_add=True)
    # auto_now will automatically update the date when saving an object (tracks last modification time)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT,
    )

    # This class defines metadata for the model
    class Meta:
        # This order takes effect unless a specific order is indicated in the query
        ordering = ['-publish'] # We can indicate descending order by using a hyphen before the field name
        indexes = [
            models.Index(fields=['-publish']), # The index will be generated in descending order
        ]

    # Django uses this method to return a string with the human-readable representation of the object
    def __str__(self):
        return self.title