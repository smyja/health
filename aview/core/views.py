from django.contrib.auth import login, authenticate, logout ,get_user_model
from .forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Appointment
from .decorators import allowed_users
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import account_activation_token
from django.template.loader import render_to_string

from .forms import SignUpForm,PatientForm
from .tokens import account_activation_token
# Create your views here.
def homepage(request):
    return render(request, 'core/frontpage.html')

def login_user(request):
    if request.method == 'POST':
        usernayme = request.POST.get('Username')
        password = request.POST.get('Password')
        try:
            username = Profile.objects.get(email=usernayme).user
        except Profile.DoesNotExist:
            username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)
        print(username,password,user)
        if user is None:
            messages.success(request, 'Username or Password is incorrect')
            return redirect('login')
        else:
            login(request, user)
            group = None
            if user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'Hospitals':
                
                return redirect('hospital')
            

            

            return redirect('dashboard')

    else:
        context = {}

        return render(request, 'core/login.html', context)


def addpatient(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.middle_name = form.cleaned_data.get('middle_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.state = form.cleaned_data.get('state')
        user.profile.dob = form.cleaned_data.get('dob')
        user.profile.next_of_kin = form.cleaned_data.get('next_of_kin')
        user.profile.address = form.cleaned_data.get('address')
        user.profile.phonenumber = form.cleaned_data.get('phonenumber')
        user.is_active = True
       
        user.save()
        addapp = Appointment(hospital=request.user.profile,patient=user.profile, status='approved')
        addapp.save()



        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        messages.success(request, 'Account was created for ' + username)
        user = authenticate(username=username, password=password)
        print(username, password, user)
        login(request, user)
        return redirect(f'/dashboard/profile/{user.profile.slug}/{user.pk}')
  
    return render(request, 'core/addpatient.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('homepage')


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        print ("form is valid")
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.address = form.cleaned_data.get('address')

        user.profile.phonenumber = form.cleaned_data.get('phonenumber')
        user.is_active = False

        user.save()
        current_site = get_current_site(request)
        subject = 'Please Activate Your Account'
        message = render_to_string('core/activation_request.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        return redirect('activation_sent')

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        messages.success(request, 'Account was created for ' + username)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})





def about(request):
    return render(request, 'core/about.html')


def terms(request):
    return render(request, 'core/terms.html')


def privacy(request):
    return render(request, 'core/privacy.html')

@login_required
@allowed_users
def hospital(request):
    appointments = Appointment.objects.filter(hospital=request.user.profile).exclude(status='approved')
    appointment_number = Appointment.objects.filter(
        hospital=request.user.profile).exclude(status='book').count()
    
    context = {
        'appointments': appointments,
        'appointment_number': appointment_number,
        
    }
    return render(request, 'core/hospital.html', context)

def patients(request):
    appointments = Appointment.objects.filter(
        hospital=request.user.profile).exclude(status='book')
    appointment_number = Appointment.objects.filter(
        hospital=request.user.profile).exclude(status='book').count()

    context = {
        'appointments': appointments,
        'appointment_number': appointment_number,

    }
    return render(request, 'core/patient.html', context)


def activation_sent_view(request):
    return render(request, 'core/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('homepage')
    else:
        return render(request, 'core/activation_invalid.html')



    

