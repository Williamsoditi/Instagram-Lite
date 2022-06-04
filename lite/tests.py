from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile, Comment, Follow

# Create your tests here.

#Profile Model test
class ProfileTestClass(TestCase):
    def setUp(self):
        self.williams = User(username = 'williams', email = 'williams99@gmail.com', password = '123qwerty')
        self.profile = Profile(bio = 'bio', user = self.williams)
        self.williams.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.williams, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_search_user(self):
        user = Profile.search_user(self.williams)
        self.assertEqual(len(user), 1)

# Follow model tests
class FollowTestClass(TestCase):
    def setUp(self):
        self.williams = User(username = 'Williams', email = 'williams99@yahoo.com', password = '123qwerty')
        self.profile1 = Profile(bio = 'bio', user = self.williams)
        self.opiyo = User(username = 'opiyo', email = 'opiyo@gmail.com', password = '12345')
        self.profile2 = Profile(bio = 'bio', user = self.opiyo)
        self.williams.save()
        self.opiyo.save()
        self.follow = Follow  (followed = self.profile1, follower = self.profile2)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.follow,Follow))




