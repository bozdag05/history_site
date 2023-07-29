import re

from django.core.exceptions import ValidationError
from django.template.context_processors import media

from .models import News
from django import forms


class NewsForm(forms.ModelForm):
    '''title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.ModelChoiceField(label='Автор', queryset=Author.objects.all(), empty_label='Автор не выбран', widget=forms.Select(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана', widget=forms.Select(attrs={"class": "form-control"}))
    content = forms.CharField(label='Новость', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    photo = forms.ImageField(label='Фотография', widget=forms.FileInput(attrs={"class": 'form-control'}))'''

    class Meta:
        model = News
        fields = ['title', 'author', 'category', 'content', 'photo']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

