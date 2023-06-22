from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': "Список новостей"
    }
    return render(request, template_name='news/index.html', context=context)


def test_page(request):
    return HttpResponse('<h1>Тестовая страница</h1>')