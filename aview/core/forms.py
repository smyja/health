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
    
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': ('Username')})
        self.fields['email'].widget.attrs.update(
            {'placeholder': ('Email'), 'class': 'log'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': ('Address'), 'class': 'log'})
        self.fields['phonenumber'].widget.attrs.update(
            {'placeholder': ('Phone number'), 'class': 'log'})
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': ('First name'), 'class': 'log'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': ('Last name'), 'class': 'log'})

        self.fields['password1'].widget.attrs.update(
            {'placeholder': ('Password'), 'class': 'log swiy'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': ('Repeat password'), 'class': 'log swiy'}) 

      
     

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
        self.fields['middle_name'].widget.attrs.update(
            {'placeholder': ('Middle name')})
        
        

        self.fields['password1'].widget.attrs.update({'placeholder': ('Password')})
        self.fields['password2'].widget.attrs.update({'placeholder': ('Repeat password')})
        self.fields['dob'].widget.attrs.update({'placeholder': ('Date of birth')})
        self.fields['state'].widget.attrs.update({'placeholder': ('State')})
        self.fields['next_of_kin'].widget.attrs.update({'placeholder': ('Next of kin')})
        self.fields['first_name'].widget.attrs.update({'class': 'log'})
        self.fields['last_name'].widget.attrs.update({'class': 'log'})
        self.fields['middle_name'].widget.attrs.update({'class': 'log'})
        self.fields['email'].widget.attrs.update({'class': 'log'})
        self.fields['phonenumber'].widget.attrs.update({'class': 'log'})
        self.fields['address'].widget.attrs.update({'class': 'log'})
        self.fields['dob'].widget.attrs.update({'class': 'log'})
        self.fields['state'].widget.attrs.update({'class': 'log'})
        self.fields['next_of_kin'].widget.attrs.update({'class': 'log'})
        self.fields['username'].widget.attrs.update({'class': 'log'})
        self.fields['password1'].widget.attrs.update({'class': 'log swiy'})
        self.fields['password2'].widget.attrs.update({'class': 'log swiy'})

    class Meta:
        model = User
       
        fields = ('username', 'first_name', 'last_name', 'middle_name','phonenumber',
                  'email', 'password1', 'password2', 'address','dob','state','next_of_kin')
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
            raise forms.ValidationError('This email is already in use! Try another email.')
        return email
       
     # Add this to check if the username already exists in your database or not     
    def clean_username(self):
        username = self.cleaned_data.get('username')
        email=self.cleaned_data.get('email')
        if username and User.objects.filter(username=username).exclude(email=email).count():
            raise forms.ValidationError('This username has already been taken!')
        return username  
 

class PatientNotesForm(ModelForm):
    illness = forms.CharField(max_length=100, help_text='First Name')
    patient = forms.ModelChoiceField(queryset=Profile.objects.all())
    patientfullname = forms.CharField(max_length=1000, help_text='First Name')
    doctor = forms.CharField(max_length=100, help_text='address')
    description = forms.CharField(max_length=10000, widget=forms.Textarea)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.DateField(
            widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        self.fields['illness'].widget.attrs.update(
            {'placeholder': ('illness')})
        self.fields['doctor'].widget.attrs.update(
            {'placeholder': ("Doctor's name")})
        self.fields['patient'].widget.attrs.update(
            {'placeholder': ("Patient's name")})
        self.fields['patientfullname'].widget.attrs.update(
            {'placeholder': ("Patient's name")})
        self.fields['description'].widget.attrs.update(
            {'placeholder': ("Description")})
        self.fields['illness'].widget.attrs.update({'class': 'log'})
        self.fields['doctor'].widget.attrs.update({'class': 'log'})
        self.fields['patientfullname'].widget.attrs.update({'class': 'log','readonly':True})
        self.fields['patient'].widget.attrs.update({'class': 'log'})
        self.fields['description'].widget.attrs.update({'class': 'textarea'})

    class Meta:
        model = Note
        
        fields = ('illness', 'patient','patientfullname', 'doctor', 'description')
    


class EditProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    address = forms.CharField(max_length=100, help_text='address')
    next_of_kin = forms.CharField(max_length=100, help_text='Next of kin')
    dob = forms.CharField(max_length=100, help_text='Date of birth')
    state = forms.CharField(max_length=100, help_text='State')
    password1 = forms.CharField(required=False, max_length=100, help_text='State')
    password2 = forms.CharField(
        required=False, max_length=100, help_text='State')
    phonenumber = forms.CharField(
        max_length=100, help_text='Enter Phone number')
    email = forms.EmailField(max_length=150, help_text='Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
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

       
        self.fields['dob'].widget.attrs.update(
            {'placeholder': ('Date of birth')})
        self.fields['state'].widget.attrs.update({'placeholder': ('State')})
        self.fields['next_of_kin'].widget.attrs.update(
            {'placeholder': ('Next of kin')})
        self.fields['first_name'].widget.attrs.update({'class': 'log'})
        self.fields['last_name'].widget.attrs.update({'class': 'log'})
        self.fields['email'].widget.attrs.update({'class': 'log'})
        self.fields['phonenumber'].widget.attrs.update({'class': 'log'})
        self.fields['address'].widget.attrs.update({'class': 'log'})
        self.fields['dob'].widget.attrs.update({'class': 'log'})
        self.fields['state'].widget.attrs.update({'class': 'log'})
        self.fields['next_of_kin'].widget.attrs.update({'class': 'log'})
        
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phonenumber',
                  'email', 'address', 'dob', 'state', 'next_of_kin')

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        password = self.cleaned_data["password1"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
