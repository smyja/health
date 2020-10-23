from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser

get_user_model().objects.filter(is_superuser=True).update(first_name='Super', last_name='User')


# superusers = User.objects.filter(is_superuser=True)
class Profile(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=128, blank=True)
    next_of_kin = models.CharField(max_length=100, blank=True)
    dob = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    
    signup_confirmation = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    appointment_with = models.ManyToManyField(User, related_name='appontment_with', blank=True)
    slug = models.SlugField(max_length=200, null=True)
    
    USERNAME_FIELD ='user'

    def save(self, *args, **kw):
        self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
        super(Profile, self).save(*args, **kw)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.last_name}-{self.first_name}")
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
    def get_hospitals(self):
        return self.hospitals.all()





STATUS_CHOICES = (
    ('book', 'book'),
    ('approved', 'approved'),
)
class Appointment(models.Model):
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='patientt', null=True)
    hospital = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hospital', null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='none')



    def __str__(self):
        return f"{self.patient}-{self.hospital}-{self.status}"

class Note(models.Model):
    illness = models.CharField(max_length=1000, blank=True)
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='patientnote', null=True)
    Doctor = models.CharField(max_length=100, blank=True)
    Description = models.CharField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.illness}"

   




