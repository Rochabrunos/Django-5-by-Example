from django.urls import path
from . import views

# Define application namespace allowing to organize URLs by application adn use the name when referring to them
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:id>/', views.post_detail, name='post_detail'), # Angle brackets is used to capture the values from the URL
]