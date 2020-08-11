from django.contrib.auth.models import User
from django.dispatch import receiver,Signal
from django.db.models.signals import post_save
from .models import Profile, Appointment


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=Appointment)
def post_save_add_to_appointment_with(sender, instance, created, **kwargs):
    patient_ = instance.patient
    hospital_ = instance.hospital
    if instance.status == 'approved':
        patient_.appointment_with.add(hospital_.user)
        hospital_.appointment_with.add(patient_.user)
        patient_.save()
        hospital_.save()
