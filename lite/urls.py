from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('email/',views.email,name='email'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('profile/<user_id>',views.profile,name = 'profile'),
    path('upload/image', views.upload_image, name = "upload_image"),
    path('search/',views.search,name ='search'),
    path('like/(<image_id>\d+)', views.like_image, name = 'like_image'),
    path('comment/(<image_id>\d+)', views.comment,name = "comment"),
    path('profile/edit', views.profile_edit,name = 'profile_edit'),
]