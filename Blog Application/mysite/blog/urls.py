from django.urls import path
from . import views

# Define application namespace allowing to organize URLs by application adn use the name when referring to them
app_name = 'blog'

urlpatterns = [
    # as_view() method is used because path expect a callable function, not a class
    path('', views.PostListView.as_view(), name='post-list'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='post-list-by-tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', 
         views.post_detail, 
         name='post_detail'), # Angle brackets is used to capture the values from the URL
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]