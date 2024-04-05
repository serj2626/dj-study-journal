from django.contrib import admin
from .models import (
    Course, Staff, Subject, Student, NotificationStaff, NotificationStudent,
    FeedBackStudent, FeedBackStaff, CustomUser, AdminHOD, SessionYearModel)

from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    '''Custom User Admin'''
    pass


admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(NotificationStaff)
admin.site.register(NotificationStudent)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaff)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(AdminHOD)
admin.site.register(SessionYearModel)
