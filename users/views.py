from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DetailView
from users.forms import ProfileForm
from chat import models
from users.forms import RegisterForm
from users.models import User


# dashboard or user panel (Login Required)

'''
    we send to panel page this datas:
    message numbers
    chat room numbers
    last login
    date joined
    chat rooms
'''
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


'''
    logout user and redirect to panel page ( becouse panel is login required basicly user redirect to login page )
'''
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('panel'))


'''
    thia class based view get the form from `forms.py` file and fields
    
    now user can see inputs
    if form is valid then is posted to this page we create new user and login the user

'''
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
            """
                if user profile data is valid we send user to home page
            """
            return redirect(to='/')

        return render(request, self.template_name, {'form': form})



# Detail Profile
class Profile(LoginRequiredMixin,UpdateView,DetailView):
    model = User
    template_name = 'panel/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy("profile")
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)


'''
    get user profile page for detail of users in the chat room.
    for do this work we must get another data from user for find him.
    so we can get a username from urls and find user with this data. 
'''
def user_profile(request,username):
    # get number of user messages
    number_messages = models.Message.objects.filter(author=request.user).count()
    # get number of user chat rooms
    chatroom_number = models.Chat.objects.filter(members=request.user).count()
    # get user last login
    last_login = User.objects.get(username=request.user.username).last_login
    user = User.objects.get(username=username)
    return render(request, 'panel/user_profile.html', {'user': user,'message_number': number_messages,
        'chat_rooms_number':chatroom_number,
        'last_login':last_login,})