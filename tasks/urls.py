from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/posts/', views.get_posts, name='get_posts'),
    path('api/posts/<int:pk>/', views.update_or_delete_post, name='update_or_delete_post'),
]