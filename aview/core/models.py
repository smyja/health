from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):
    username = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    title = models.CharField(max_length=255, null=True)
    margin = models.FloatField(default=20, null=True)
    amount = models.FloatField(default=20, null=True)
    country = models.CharField(max_length=255, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    appointment_with = models.ManyToManyField(User, related_name='appontment_with', blank=True)


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

    @classmethod
    def create_appointment(cls, hospital,patient):
        try:
            appointment,created = cls.objects.get_or_create(patient=patient,hospital=hospital)
        except cls.MultipleObjectsReturned:
            appointment = cls.objects.filter(patient).order_by('id').first()

        appointment.hospital.appointment_with.add(patient.user)
        
    # @classmethod
    # def accept_appointment(cls, request,patient,status):
    #     try:
    #         appointment,created = cls.objects.get_or_create(status=status)
    #     except cls.MultipleObjectsReturned:
    #         appointment = cls.objects.filter(patient=patient,hospital=request.user.profile)

    #     appointment.status.appointment_with.update(status='approved')
        
   


        
        
        





    def __str__(self):
        return f"{self.patient}-{self.hospital}-{self.status}"


   




