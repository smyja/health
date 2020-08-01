from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Profile
from .decorators import allowed_users
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request, 'core/frontpage.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        print(username,password,user)
        if user is None:
            messages.success(request, 'Username or Password is incorrect')
            return redirect('login')
        else:
            login(request, user)

            return redirect('dashboard')
    else:
        context = {}

        return render(request, 'core/login.html', context)


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.title = form.cleaned_data.get('title')

        user.profile.country = form.cleaned_data.get('country')
        user.profile.phonenumber = form.cleaned_data.get('phonenumber')
        user.is_active = True

        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        messages.success(request, 'Account was created for ' + username)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('homepage')


def about(request):
    return render(request, 'core/about.html')


def terms(request):
    return render(request, 'core/terms.html')


def privacy(request):
    return render(request, 'core/privacy.html')

@login_required
@allowed_users
def hospital(request):
    return render(request, 'core/hospital.html')

