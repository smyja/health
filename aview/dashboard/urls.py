from django.urls import path, re_path
from .views import dashboard, profile, bookapp, acceptapp



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
        bookapp, name='bookapp'),
]
