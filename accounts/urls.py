from django.urls import path
from .views import MyProfileUpdateView


app_name = 'accounts'


urlpatterns = [
    # path('login/', 'login', name='login'),
    # path('logout/', 'logout', name='logout'),
    # path('signup/', 'signup', name='signup'),
    path('profile/', MyProfileUpdateView.as_view(), name='my_profile'),
]
