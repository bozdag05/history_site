import re
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.template.context_processors import media
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import News
from django import forms
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Пользователь', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={"class": "form-control"})),
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            validate_password(password1)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


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

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={"class": "form-control"}))
    captcha = CaptchaField()
