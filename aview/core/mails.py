from simple_mail.mailer import BaseSimpleMail, simple_mailer

class WelcomeMail(BaseSimpleMail):
    email_key = 'lcomieuer'

welcome_mail = WelcomeMail()
simple_mailer.register(WelcomeMail)
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Note


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    address = forms.CharField(max_length=100, help_text='address')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phonenumber',
                'email', 'password1', 'password2', 'address')
    # Add this to check if both passwords are matching or not
    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email is already in use! Try another email.')
        return email


class PatientForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    middle_name = forms.CharField(max_length=100, help_text='Middle Name')
    address = forms.CharField(max_length=100, help_text='address')
    next_of_kin = forms.CharField(max_length=100, help_text='Next of kin')
    dob = forms.DateField(help_text='Date of birth',
                          widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    state = forms.CharField(max_length=100, help_text='State')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User

        fields = ('username', 'first_name', 'last_name', 'middle_name', 'phonenumber',
                  'email', 'password1', 'password2', 'address', 'dob', 'state', 'next_of_kin')

    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        password = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match!')

    # Add this to check if the email already exists in your database or not

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(
                'This email is already in use! Try another email.')
        return email

     # Add this to check if the username already exists in your database or not
    def clean_username(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if username and User.objects.filter(username=username).exclude(email=email).count():
            raise forms.ValidationError(
                'This username has already been taken!')
