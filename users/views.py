from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from chat import models
from users.forms import RegisterForm
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

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'panel/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})