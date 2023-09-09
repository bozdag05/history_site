from datetime import date

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    tagline = models.TextField(max_length=500, verbose_name='Загаловок', null=True, blank=True)
    premiere = models.DateField(max_length=150, verbose_name='Премьера', default='Неизвестно')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    age_rating = models.ForeignKey('RatingAge', verbose_name='Возрастной рейтинг', null=True, on_delete=models.SET_NULL, default='Неопределено')
    country = models.ManyToManyField('Country', verbose_name='Страна')
    actor = models.ManyToManyField('Actor', verbose_name='Актёр', related_name='film_actor')
    director = models.ManyToManyField('Actor', verbose_name='Режиссер', related_name='film_director')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    poster = models.ImageField(verbose_name='Постер', upload_to='media/movie/%Y/%m/%d/')
    year = models.DateField(verbose_name='Год выпуска', default=date.today)
    duration = models.SmallIntegerField(verbose_name='Продолжительность')
    budget = models.PositiveSmallIntegerField(verbose_name='Бюджет', null=True, blank=True)
    url = models.SlugField(verbose_name='Слаг', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    is_published = models.BooleanField(verbose_name='Публикация', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-created_at']


class Actor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    biography = models.TextField(verbose_name='Биография', null=True, blank=True)
    birth_date = models.DateField(verbose_name='День рождения')
    death_date = models.DateField(verbose_name='День смерти')
    country = models.CharField(max_length=150, verbose_name='Страна')
    photo = models.ImageField(verbose_name='Изображение', upload_to='media/actors/%Y/%m/%d/')
    is_published = models.BooleanField(verbose_name='Публикация', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёр и Режиссер'
        verbose_name_plural = 'Актёры и Режисёры'


class Genre(models.Model):
    title = models.CharField(max_length=150, verbose_name='Жанр')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class RatingAge(models.Model):
    age_rating = models.CharField(max_length=30, verbose_name='Возрастной рейтинг')

    def __str__(self):
        return self.age_rating

    class Meta:
        verbose_name = 'Возрастной рейтинг'
        verbose_name_plural = 'Возрастные рейтингы'


class Country(models.Model):
    country = models.CharField(max_length=150, verbose_name='Страна')
    description = models.TextField(verbose_name='Страны')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class MovieShot(models.Model):
    title = models.CharField(max_length=150, verbose_name='Загаловок')
    image = models.ImageField(verbose_name='Кадр', upload_to='media/shots/%Y/%m/%d/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    value = models.SmallIntegerField(verbose_name='Значение')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звёзды рейтинга'


class Rating(models.Model):
    ip = models.CharField(verbose_name='IP адресс', max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name='Звезда', on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    text_review = models.TextField(verbose_name='Отзыв', max_length=3000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'