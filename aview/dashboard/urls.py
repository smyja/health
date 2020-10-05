from django.urls import path, re_path
from .views import dashboard, profile, bookapp, acceptapp, edit_profile



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('profile/<str:slug>/<int:pk>', profile, name='profilepk'),
    path('edit_profile/<int:id>/', edit_profile, name='editprofile'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
        bookapp, name='bookapp'),
]
