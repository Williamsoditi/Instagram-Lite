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

class CommentTestClass(TestCase):
    def setUp(self):
        self.williams = User(username = "williams", email = "williamsoditi99@gmail.com",password = "123qwerty")
        self.profile = Profile(bio='bio', user= self.williams)
        self.basketball = Image(image = 'imageurl', name ='basketball', caption = 'Clique Mambas causing Havoc', profile = self.profile)
        self.comment = Comment(image=self.basketball, content= 'Killer instinct', user = self.williams)

        self.williams.save()
        self.profile.save()
        self.basketball.save_image()
        self.comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        comments = Comment.get_image_comments(self.basketball)
        self.assertEqual(comments[0].content, 'Killer instinct')
        self.assertTrue(len(comments) > 0)


