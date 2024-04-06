from django.contrib import admin
from .models import (
    Course, Teacher, Subject, Student, NotificationTeacher, NotificationStudent,
    FeedBackStudent, FeedBackTeacher, CustomUser, AdminHOD, SessionYearModel)

from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    '''Custom User Admin'''
    pass


admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(NotificationTeacher)
admin.site.register(NotificationStudent)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackTeacher)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(AdminHOD)
admin.site.register(SessionYearModel)
