from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    country = forms.CharField(max_length=100, help_text='Country of residence')
    address = forms.CharField(max_length=100, help_text='address')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')
    
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'placeholder': ('Username')})
        self.fields['email'].widget.attrs.update(
        {'placeholder': ('Email')})
        self.fields['address'].widget.attrs.update(
            {'placeholder': ('Address')})
        self.fields['phonenumber'].widget.attrs.update(
            {'placeholder': ('Phone number')})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': ('First name')})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': ('Last name')})




        self.fields['password1'].widget.attrs.update({'placeholder': ('Password')})
        self.fields['password2'].widget.attrs.update({'placeholder': ('Repeat password')})
        self.fields['first_name'].widget.attrs.update({'class': 'log'})
        self.fields['last_name'].widget.attrs.update({'class': 'log'})
        self.fields['email'].widget.attrs.update({'class': 'log'})
        self.fields['phonenumber'].widget.attrs.update({'class': 'log'})
        self.fields['address'].widget.attrs.update({'class': 'log'})
        self.fields['username'].widget.attrs.update({'class': 'log'})
        self.fields['password1'].widget.attrs.update({'class': 'log swiy'})
        self.fields['password2'].widget.attrs.update({'class': 'log swiy'})



    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phonenumber',
                  'email', 'password1', 'password2', 'country')
    
 


