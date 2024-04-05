from django.urls import path
from .views import (
    HomeView, StudentsMyGroupListView, MyMarksListView,
    ChatView, TeachersListView, FeedBackStudentCreateView,
    NotificationStudentView)


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('students-my-group/', StudentsMyGroupListView.as_view(),
         name="students_my_group"),
    path('my-marks/', MyMarksListView.as_view(), name="my_marks"),
    path('chat/', ChatView.as_view(), name="chat"),
    path('teachers/', TeachersListView.as_view(), name="teachers_list"),
    path('feedback-student-create/', FeedBackStudentCreateView.as_view(),
         name="feedback_student_create"),
    path('notification-student/', NotificationStudentView.as_view(),name="notification_student"),
]
