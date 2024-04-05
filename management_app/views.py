from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from common.utils import TitleMixin
from management_app.models import FeedBackStudent
from .forms import FeedBackStudentForm, FeedBackStaffForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class HomeView(TitleMixin, TemplateView):
    title = 'Главная'
    template_name = 'management_app/home.html'


class StudentsMyGroupListView(TitleMixin, TemplateView):
    title = 'Список одногруппников'
    template_name = 'management_app/students_list.html'


class MyMarksListView(TitleMixin, TemplateView):
    title = 'Мои оценки'
    template_name = 'management_app/marks_list.html'


class ChatView(TitleMixin, TemplateView):
    title = 'Чат'
    template_name = 'management_app/chat.html'


class TeachersListView(TitleMixin, TemplateView):
    title = 'Преподаватели'
    template_name = 'management_app/teachers_list.html'


class FeedBackStudentCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    title = 'Обратная связь'
    model = FeedBackStudent
    form_class = FeedBackStudentForm
    template_name = 'management_app/feedback_student.html'
    success_message = 'Спасибо за обратную связь'
    success_url = reverse_lazy('home')


class NotificationStudentView(TitleMixin, TemplateView):
    title = 'Уведомления'
    template_name = 'management_app/notification_student.html'

class NotificationStaffView(TitleMixin, TemplateView):
    title = 'Уведомления'
    template_name = 'management_app/notification_staff.html'