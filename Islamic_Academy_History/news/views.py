from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    authors = Author.objects.all()
    context = {
        'news': news,
        'categories': categories,
        'authors': authors,
        'title': "Список новостей",
        'title_category': "Список категории",
        'title_author': "Список авторов",
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    category_news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    authors = Author.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'category_news': category_news,
        'categories': categories,
        'category': category,
        'authors': authors,
        'title_category': "Список категории",
        'title_author': "Список авторов",
    }
    return render(request, template_name='news/category_news.html', context=context)


def get_author(request, author_id):
    categories = Category.objects.all()
    author_news = News.objects.filter(author_id=author_id)
    authors = Author.objects.all()
    context = {
        'categories': categories,
        'author_news': author_news,
        'authors': authors,
        'title_category': "Список категории",
        'title_author': "Список авторов",
    }
    return render(request, template_name='news/author_news.html', context=context)
