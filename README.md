# Django Super Channels
Chat room web application based on `django_super_channels` and implemented with websockets protocol.

[![Python](https://img.shields.io/badge/python-%2320232a.svg?style=for-the-badge&logo=python)](#django-channels)
[![Django](https://img.shields.io/badge/django-%2320232a.svg?style=for-the-badge&logo=django)](#django-channels)
[![redis](https://img.shields.io/badge/redis-%2320232a.svg?style=for-the-badge&logo=redis)](#django-channels)
[![Sqlite](https://img.shields.io/badge/sqlite-%2320232a.svg?style=for-the-badge&logo=sqlite)](#django-channels)
[![djangorestframework](https://img.shields.io/badge/Django_Rest_Framework-%2320232a.svg?style=for-the-badge&logo=fastapi)](#django-channels)
[![js](https://img.shields.io/badge/java_script-%2320232a.svg?style=for-the-badge&logo=javascript)](#django-channels)

**Django Super Channels** is a chat room application based on django-channels.
The design of this application is group chat.
# Work process
The design and operation process of super channels is such that the address of the chat room is received on the index page. (if the chat room is available, it will be entered, and if it is not available, the chat room will be created).
After the person enters the room, you can communicate with the people who have entered the chat room.
<center><img src="static/img/readme.png" width="100%"></center>

According to the picture, when a message is sent from the `mahdi` user, the message is sent to the server through websocket.
The server saves the message once in the database and sends the same message again to the mahdi user and other users without the need for a request.
All messages are received in the form of json through the client, and the main part of designing and displaying the messages is the responsibility of the client.

`django channels` is designed in the form of a messenger application whose client is javascript and its back-end has created a websocket-based connection with django.




## Performance

> [!NOTE]
> It is better to use the **virtualenvironment** when installing libraries and running the project. 


> [!WARNING]
> Have **redis** installed on the system before running. <br>
> download and install [redis for windows](https://github.com/tporadowski/redis/releases) and to `cmd` type `redis-server` to run the redis.

**To install required libraries:**
```
pip install -r requirements.txt
```

**To Run The Project:**
```
python manage.py runserver
```

<hr>

> Not yet evolved

Comming Soon
