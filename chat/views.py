from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def index(request):
    return render(request, "chat/index.html")


@login_required()
def room(request, room_name):

    context = {
        "room_name": room_name,
    }

    return render(request, "chat/room.html", context)