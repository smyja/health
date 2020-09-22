from django.contrib.auth import get_user_model
from django.test import TestCase
from django.shortcuts import reverse
from aview.core.models import Appointment, Profile

User = get_user_model()

class BookinTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        patient = User.objects.create_user("test2", "", "test1234")
        
        hospital = User.objects.create_user("test5", "", "test1234")
        patient = Profile.objects.get(user_id=1)
        hospital = Profile.objects.get(user_id=2)
        ao = Appointment(hospital=hospital, patient=patient)
        patient.appointment_with.add(hospital.user)
        hospital.appointment_with.add(patient.user)
        ao.save()
        
        # addapp = Appointment(hospital=hospital, patient=request.user.profile)

 
    def test_appointment_view(self):
        hospital = Profile.objects.get(user_id=2)
        context = {'hospitalt': hospital}
        response = self.client.post('/book',context,secure=True,follow=True)
        self.assertEqual(response.status_code, 200)

        

