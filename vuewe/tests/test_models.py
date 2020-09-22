from django.contrib.auth import get_user_model
from django.test import TestCase
from aview.core.models import Profile


User = get_user_model()


class ProfileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("test","", "test1234")
    
    def setUp(self):
        self.user = User.objects.get(username="test")
        
    def test_create_profile(self):
        userprofile = Profile.objects.get(user=self.user)

        """Check if the profile model is the right one """
        self.assertTrue(isinstance(userprofile, Profile))

        """Check if it returns the username"""
        self.assertEqual(userprofile.__str__(), self.user.username)

