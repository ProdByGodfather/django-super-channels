from django.db import models
from django.contrib.auth import get_user_model

# User Authenticated
User = get_user_model()

# Create Model Chat
class Chat(models.Model):
    roomname = models.CharField(max_length=75,blank=True)
    members = models.ManyToManyField(User, null=True,blank=True)
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.roomname





# Create Model Message
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def last_messages(self):
        return Message.objects.order_by('-timestamp').all()
    def __str__(self):
        return self.author.username
