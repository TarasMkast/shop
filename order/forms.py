from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    email = forms.EmailField(help_text='Вкажіть вашу електронну пошту', label='Електронна пошта',
                             error_messages={'required': ''})
    first_name = forms.CharField(help_text='Вкажіть ваше імя', label='Імя', error_messages={'required': ''})
    last_name = forms.CharField(help_text='Вкажіть ваше прізвище', label='Прізвище', error_messages={'required': ''})
    city = forms.CharField(help_text='Вкажіть ваше місто проживання', label='Місто', error_messages={'required': ''})
    address = forms.CharField(help_text='Вкажіть вашу адресу проживання, наприклад : "Мазепи 42"', label='Адреса',
                              error_messages={'required': ''})

    class Meta:
        model = Order
        fields = ['email', 'first_name', 'last_name', 'city', 'address']
