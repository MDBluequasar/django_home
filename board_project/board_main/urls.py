from django.urls import path
from django.urls import include
from .import views


urlpatterns = [
    path('', views.home),
    path('author/', views.author_list),
    path('author/new', views.author_new),
    path('author/<int:my_id>', views.author_detail),
    path('author/<int:my_id>/update', views.author_update),
    path('posts/', views.post_list),
    path('post/new', views.post_new),
    path('post/<int:my_id>', views.post_detail),
    path('post/<int:my_id>/update', views.post_update),
]
