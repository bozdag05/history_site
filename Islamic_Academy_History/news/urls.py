from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib import admin
from .views import *

urlpatterns = [
    path('test/', user_callback, name='test'),
    path('', cache_page(60)(HomeNews.as_view()), name='home'),
    path('category/<int:category_id>', CategoryNews.as_view(), name='category'),
    path('author/<int:author_id>', AuthorNews.as_view(), name='author'),
    path('news/<int:news_id>', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('news/register', register, name='register'),
    path('news/login', user_login, name='login'),
    path('news/logout', user_logout, name='logout'),
]