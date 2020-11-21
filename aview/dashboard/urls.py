from django.urls import path, re_path
from .views import dashboard, profile, bookapp, acceptapp,edit_profile,addnotes,notes,viewnotes



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('profile/<str:slug>/<int:pk>', profile, name='profilepk'),
    path('edit_profile/<str:slug>/<int:id>/', edit_profile, name='editprofile'),
    path('addnotes/<str:slug>/<int:id>', addnotes, name='addnote'),
    path('notes/<str:slug>/<int:id>', notes, name='notes'),
    path('readnotes/<str:slug>/<int:id>/<int:pk>/', viewnotes, name='viewnotes'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
        bookapp, name='bookapp'),
]
