from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    # login auth user model
    path("login", auth_views.LoginView.as_view(template_name='chat/login.html'),name='login')
]