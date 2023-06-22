from django.contrib import admin
from .models import News, Category, Author


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published', 'author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name', 'data_birth', 'data_death')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
