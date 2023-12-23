from enum import member

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from chat import models

@login_required()
def index(request):
    # get user
    user = request.user
    # get user chatrooms
    chat_rooms = models.Chat.objects.filter(members = user)

    context = {
        'chat_rooms':chat_rooms,
    }


    return render(request, "chat/index.html",context)


@login_required()
def room(request, room_name):
    chat_model = models.Chat.objects.filter(roomname=room_name)

    if not chat_model.exists():
        chat = models.Chat.objects.create(roomname=room_name)
        chat.members.add(request.user)
    else:
        chat_model[0].members.add(request.user)

    context = {
        "room_name": room_name,
    }

    return render(request, "chat/room.html", context)