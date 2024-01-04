from enum import member

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from chat import models

'''
    login required
    
    this function send user to index chat page
    this page shows to user chat rooms and a input for create chat rooms
    
    basicly this page expired
'''
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



'''
    index chat room page
'''
@login_required()
def room(request, room_name):
    chat_model = models.Chat.objects.filter(roomname=room_name)

    if not chat_model.exists():
        chat = models.Chat.objects.create(roomname=room_name)
        chat.members.add(request.user)
    else:
        chat_model[0].members.add(request.user)

    members_list =  chat_model[0].members.all()

    usernumber = len(members_list)
    context = {
        "room_name": room_name,
        'chat_model': chat_model,
        'members_list': members_list,
        'usernumber':usernumber
    }
    return render(request, "chat/room.html", context)



'''
    this is new function
    users can delete chat room for her selves
    just chat room never show on user panel
'''
def del_room(request, room_name):
    user = request.user
    cat = models.Chat.objects.get(roomname=room_name)
    cat.members.remove(user)
    return HttpResponseRedirect(reverse_lazy('panel'))

