from django.http import HttpResponse
from django.shortcuts import render, redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(view_func):
    def wrapper_function(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'Hospitals':
            return render(request, 'core/hospital.html')
        else:
            return HttpResponse('You are not authorised to access this page')

        return view_func(request, *args, **kwargs)
    return wrapper_function
