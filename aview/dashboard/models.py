from django.db import models
from aview.core.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.


class Appointment1(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    appointment_with = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.appointment_with
    
    

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)


