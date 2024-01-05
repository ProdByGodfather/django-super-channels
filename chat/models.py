from django.db import models
from django.contrib.auth import get_user_model


# User Authenticated
User = get_user_model()

# Create Model Chat
'''
    chat models have a room name for get message from were room
    members can only be viewed once
    create time for show to user when message is send
'''
class Chat(models.Model):
    roomname = models.CharField(max_length=75,blank=True)
    members = models.ManyToManyField(User, null=True,blank=True)
    createtime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.roomname





# Create Model Message
'''
    every message have one chat.
    every message have one author.
    every message have content ( this content maybe base64 image or text )
    every message have an image ( this image save from author image )
'''
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    related_chat = models.ForeignKey(Chat, on_delete=models.CASCADE,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=500, blank=True,null=True)

    def last_messages(self, roomname):
        return Message.objects.filter(related_chat__roomname = roomname).order_by('-timestamp').all()

    def __str__(self):
        return self.author.username
