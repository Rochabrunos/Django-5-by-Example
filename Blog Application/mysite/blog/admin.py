from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Allows to set the field of the model is going to be displayed on admin list page
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # Allows to filter the results by the fields included in the list_filter
    list_filter = ['status', 'created', 'publish', 'author']
    # Defines a list of searchable fields
    search_fields = ['title', 'body']
    # Tells to Django to populate the slug field with the input of the title field
    prepopulated_fields = {'slug': ('title',)}
    # Display a lookup widget to search for specific user
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']