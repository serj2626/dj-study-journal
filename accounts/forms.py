from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from management_app.models import Student, Teacher

User = get_user_model()


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class SignUPForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']


class StudentProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Дата рождения',
                                    widget=MyDateInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ('phone', 'date_of_birth', 'gender', 'avatar', 'address',)
