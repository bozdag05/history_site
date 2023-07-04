from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': "Список новостей",
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    category_news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'category_news': category_news,
        'category': category,
    }
    return render(request, template_name='news/category_news.html', context=context)


def get_author(request, author_id):
    author_news = News.objects.filter(author_id=author_id)
    context = {
        'author_news': author_news,
    }
    return render(request, template_name='news/author_news.html', context=context)


def view_news(request, news_id):
    item_news = get_object_or_404(News, pk=news_id)
    return render(request, template_name='news/view_news.html', context={'item_news': item_news})