from django.urls import path
from .views import dashboard,profile


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    # path('add', addfriend, name='addfriend'),
]
