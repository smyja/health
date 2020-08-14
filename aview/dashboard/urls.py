from django.urls import path, re_path
from .views import dashboard, profile, bookapp, acceptapp



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('profile/<str:slug>/<int:pk>', profile, name='profilepk'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
        bookapp, name='bookapp'),
]
