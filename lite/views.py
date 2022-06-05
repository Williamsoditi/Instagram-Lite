from django.shortcuts import render, redirect
from .models import Image, Profile, Comment, Follow
from .forms import CreateProfileForm, UploadImageForm, FollowForm, UnfollowForm, EditBioForm
from django.http import HttpResponseRedirect, Http404
from .emails import send_signup_email
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'create-profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email(name, email)
    return redirect(create_profile)
