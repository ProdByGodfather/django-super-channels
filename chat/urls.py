from django.urls import path
from . import views
from users.views import panel

urlpatterns = [
    # this func has returned another view. new its expired
    # path("", views.index, name="index"),
    path("", panel, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("<str:room_name>/delete", views.del_room, name="del_room"),


]