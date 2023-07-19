from django.urls import path

from django.contrib import admin
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>', CategoryNews.as_view(), name='category'),
    path('author/<int:author_id>', AuthorNews.as_view(), name='author'),
    path('news/<int:news_id>', view_news, name='view_news'),
    path('news/add-news/', add_news, name='add_news'),
]