import json
from chat.models import Message
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.serializers import MessageSerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model
from chat import models

user = get_user_model()
class ChatConsumer(WebsocketConsumer):

    def new_message(self, data):
        '''
            we get message from client.
            we get request.user and time to send message
            then create new message on db
            before create new message we send data from websocket to client again
        '''
        message = data['message']
        author = data['username']
        roomname = data['roomname']
        self.notif(data)
        chat_model = models.Chat.objects.get(roomname=roomname)

        user_model = user.objects.filter(username=author).first()
        try:
            message_model = Message.objects.create(author=user_model, content=message, related_chat=chat_model,image=user_model.image.url)
        except:
            message_model = Message.objects.create(author=user_model, content=message, related_chat=chat_model,
                                                   image="/static/images/Sample_User_Icon.png")

        result = eval(self.message_serializer(message_model))
        self.send_to_chat_message(result)


    def notif(self, data):
        message_room_name = data['roomname']
        chat_room_qs = models.Chat.objects.filter(roomname=message_room_name)


        members_list = []

        for i in chat_room_qs[0].members.all():
            members_list.append(i.username)

        async_to_sync(self.channel_layer.group_send)(
            'chat_listener',
            {
                '__str__': data['username'],
                "type": "chat.message",
                "content": data['message'],
                'roomname': message_room_name,
                'members_list': members_list,
            })


    def fetch_message(self, data):
        roomname = data['roomname']
        qs = Message.last_messages(self,roomname)

        for i in qs:
            user_image = user.objects.get(username=i.__str__())
            if user_image.image == "":
                i.__dict__.update({"image": "/static/images/Sample_User_Icon.png"})
            else:
                i.__dict__.update({"image": user_image.image})


        message_json = self.message_serializer(qs)

        # message = json.loads(message_json)
        # print(message)


        # message_json += {'image':user_image}
        content = {
            "message": eval(message_json),
            'command':"fetch_message",
            # 'image':user_image.image.url
        }
        '''
            we get datas from db and show to users
        '''
        self.chat_message(content)


    def image(self,data):
        # self.send_to_chat_message(data)
        self.new_message(data)

    def message_serializer(self, qs):
        serialized = MessageSerializer(qs,many=(lambda qs: True if (qs.__class__.__name__ == 'QuerySet') else False)(qs))
        content = JSONRenderer().render(serialized.data)
        return content


    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    commands = {
        "new_message": new_message,
        "fetch_message": fetch_message,
        "img": image,
    }


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        command = text_data_json["command"]

        '''
            we get command from client
            if command was "new_message" run funtion new_message
            if command was "fetch_message" run function fetch_message 
            if command was "img" run function image
        '''
        self.commands[command](self,text_data_json)

    def send_to_chat_message(self, message):
        # Send message to room group

        command = message.get('command',None)
        timestamp = message.get('timestamp',None)
        user_image = user.objects.get(username = message['__str__'])

        try:
            async_to_sync(self.channel_layer.group_send)(self.room_group_name,
                                                         {
                                                             '__str__': message['__str__'],
                                                             'timestamp': timestamp,
                                                             "type": "chat.message",
                                                             "content": message['content'],
                                                             'image': user_image.image.url,
                                                             '''
                                                                 from command we nows what if cmmand has img or command has new_message(text)
                                                             '''
                                                             'command': (lambda command: 'img' if (
                                                                         command == 'img') else "new_message")(command),
                                                         })
        except:
            async_to_sync(self.channel_layer.group_send)(self.room_group_name,
                                                         {
                                                             '__str__': message['__str__'],
                                                             'timestamp': timestamp,
                                                             "type": "chat.message",
                                                             "content": message['content'],
                                                             '''
                                                                 from command we nows what if cmmand has img or command has new_message(text)
                                                             '''
                                                             'command': (lambda command: 'img' if (
                                                                         command == 'img') else "new_message")(command),
                                                         })

    # Receive message from room group
    def chat_message(self, event):
        self.send(text_data=json.dumps(event))