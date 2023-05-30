from django import forms
from .models import *


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите ваше фамилию'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Введите ваше отчество'}),
            'age': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.TextInput(attrs={'placeholder': 'Адрес по прописке'}),
            'real_address': forms.TextInput(attrs={'placeholder': 'Фактический адрес'}),
            'education': forms.TextInput(attrs={'placeholder': 'В каком колледже, техникуме лицее вы учитесь?'}),
            'course': forms.NumberInput(attrs={'placeholder': 'На каком вы курсе?'}),
            'speciality': forms.TextInput(attrs={'placeholder': 'Cпециальность'}),
            'contact_dad': forms.TextInput(attrs={'placeholder': 'Контакты отца'}),
            'contact_mam': forms.TextInput(attrs={'placeholder': 'Контакты матери'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Коментарий'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Ваши контактные данные'}),
            'email': forms.EmailInput(attrs={'placeholder': 'test@test.com'}),
            # 'created_date': forms.TextInput(attrs={'placeholder': 'В каком колледже, техникуме лицее вы учитесь?'}),
        }


