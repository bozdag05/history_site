from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
>>>>>>> tik-001
from .models import News, Category, Author
from django import forms


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'author', 'category', 'created_at', 'updated_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published', 'author')

    fields = ('title', 'author', 'category', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at',)
    readonly_fields = ('get_photo', 'created_at', 'updated_at',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'Миниатюра'



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
<<<<<<< HEAD
=======
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import News, Category, Author
from django import forms


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'author', 'category', 'created_at', 'updated_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published', 'author')

    fields = ('title', 'author', 'category', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at',)
    readonly_fields = ('get_photo', 'created_at', 'updated_at',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'Миниатюра'



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
=======
>>>>>>> tik-001


admin.site.site_title = 'Управление Академией'
admin.site.site_header = 'Управление Академией'

<<<<<<< HEAD
>>>>>>> abbc309199e5261d66b9e8cbdca1a0d2f0ddf2b9
=======
>>>>>>> tik-001
