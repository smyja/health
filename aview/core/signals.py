from django.contrib.auth.models import User
from django.dispatch import receiver,Signal
from django.db.models.signals import post_save
from .models import Profile, Appointment

@receiver(post_save, patient=Appointment)
def post_save_add_to_appointment_with(patient, created, instance, **kwargs):
    patient_ = instance.patient
    hospital_ = instance.hospital
    if instance.status == 'approved':
        patient_.appointment_with.add(patient_.User)
        hospital_.appointment_with.add(hospital_.User)
        patient_.save()
        hospital_.save()
