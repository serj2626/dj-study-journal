from django.shortcuts import render
from django.urls import reverse_lazy
from management_app.models import Student
from .forms import StudentProfileForm
from common.utils import TitleMixin
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


class MyProfileUpdateView(TitleMixin, SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('home')
    success_message = 'Профиль успешно обновлен'
    title = 'Мой Профиль'
