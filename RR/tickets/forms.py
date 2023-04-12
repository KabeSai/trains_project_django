from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TicketSearchForm(forms.Form):
    departure_city = forms.CharField(
        label='Откуда',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Откуда'})
    )
    arrival_city = forms.CharField(
        label='Куда',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Куда'})
    )
    departure_date = forms.DateField(
        label='Туда',
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Туда', 'onfocus': "(this.type='date')", 'onblur': "(this.type='text')"})
    )
    arrival_date = forms.DateField(
        label='Обратно',
        required=False,
        widget=forms.DateInput(attrs={'placeholder': 'Обратно', 'onfocus': "(this.type='date')", 'onblur': "(this.type='text')"})
    )


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    surname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'surname', 'email', 'number', 'password1', 'password2')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
