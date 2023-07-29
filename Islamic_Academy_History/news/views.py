from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from .forms import NewsForm
from .models import *


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

'''def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': "Список новостей",
    }
    return render(request, template_name='news/index.html', context=context)
'''


class CategoryNews(ListView):
    model = News
    template_name = 'news/category_news.html'
    context_object_name = 'category_news'
    paginate_by = 2
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


'''def get_category(request, category_id):
    category_news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'category_news': category_news,
        'category': category,
    }
    return render(request, template_name='news/category_news.html', context=context)
'''


'''def get_author(request, author_id):
    author_news = News.objects.filter(author_id=author_id)
    context = {
        'author_news': author_news,
    }
    return render(request, template_name='news/author_news.html', context=context)'''


class AuthorNews(ListView):
    model = News
    template_name = 'news/author_news.html'
    context_object_name = 'author_news'
    paginate_by = 2
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Author.objects.get(pk=self.kwargs['author_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(author_id=self.kwargs['author_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'item_news'
    pk_url_kwarg = 'news_id'


'''def view_news(request, news_id):
    item_news = get_object_or_404(News, pk=news_id)
    return render(request, template_name='news/view_news.html', context={'item_news': item_news})
'''


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'



'''def add_news(request):
    if request.method == 'POST':
        forms = NewsForm(request.POST, request.FILES)
        if forms.is_valid():
            #news = News.objects.create(**forms.cleaned_data)
            news = forms.save()
            return redirect(news)
    else:
        forms = NewsForm()
    return render(request, template_name='news/add_news.html', context={'forms': forms})'''


def test(request):
    drf = News.objects.all()
    paginator = Paginator(drf, 3)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.page(page_num)
    context = {
        'page_obj': page_obj,
        'title': 'Test_Page',
    }
    return render(request, 'news/test.html', context=context)
