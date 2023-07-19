from django import template

from news.models import Category, Author

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def get_information_for_sidebar():
    categories = Category.objects.all()
    authors = Author.objects.all()
    return {'categories': categories, 'authors': authors, 'title_category': "Список по категориям", 'title_author': "Список по авторам",}


