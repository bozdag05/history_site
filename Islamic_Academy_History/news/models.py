from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    biography = models.TextField(blank=True, null=True, verbose_name='Биография')
    data_birth = models.DateField(blank=True, null=True, verbose_name='дата рождения')
    data_death = models.DateField(blank=True, null=True, verbose_name='дата смерти')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True,  verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=0, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



