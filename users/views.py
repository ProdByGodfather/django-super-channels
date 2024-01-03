from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from chat import models
from users.models import User


# dashboard or user panel (Login Required)
@login_required()
def panel(request):
    # get number of user messages
    number_messages = models.Message.objects.filter(author = request.user).count()
    # get number of user chat rooms
    chatroom_number = models.Chat.objects.filter(members = request.user).count()
    # get user last login
    last_login = User.objects.get(username=request.user.username).last_login
    # get user date joined
    date_joined = User.objects.get(username=request.user.username).date_joined
    # get chat rooms
    chat_rooms = models.Chat.objects.filter(members= request.user)
    context = {
        'message_number': number_messages,
        'chat_rooms_number':chatroom_number,
        'last_login':last_login,
        'date_joined':date_joined,
        "chat_rooms":chat_rooms,
    }
    return render(request,'panel/panel.html',context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('panel'))
