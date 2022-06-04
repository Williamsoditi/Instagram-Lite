from django.forms import ModelForm
from .models import Profile, Follow, Image

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['created', 'account_holder', 'followers', 'following']

class FollowForm(ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']

class UnfollowForm(ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']

class UploadImageForm(ModelForm):
    class Meta :
        model = Image
        exclude = ['profile', 'post_date', 'likes']