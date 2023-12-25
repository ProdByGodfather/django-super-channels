# Django Channels
Chat room web application based on `django_channels` and implemented with websockets protocol.

[![Python](https://img.shields.io/badge/python-%2320232a.svg?style=for-the-badge&logo=python)](#django-channels)
[![Django](https://img.shields.io/badge/django-%2320232a.svg?style=for-the-badge&logo=django)](#django-channels)
[![redis](https://img.shields.io/badge/redis-%2320232a.svg?style=for-the-badge&logo=redis)](#django-channels)
[![Sqlite](https://img.shields.io/badge/sqlite-%2320232a.svg?style=for-the-badge&logo=sqlite)](#django-channels)
[![djangorestframework](https://img.shields.io/badge/Django_Rest_Framework-%2320232a.svg?style=for-the-badge&logo=fastapi)](#django-channels)
[![js](https://img.shields.io/badge/java_script-%2320232a.svg?style=for-the-badge&logo=javascript)](#django-channels)

Channels support Django's native asynchronous view and allow Django projects to handle not only HTTP, but also protocols that require long-running connections - `WebSockets`, `MQTT`, `chatbots`, `amateur radio`, `etc`.
Now the django_channels architecture allows us to use websockets.
Protocols that provide the possibility of sending requests from both the server and the client side.

<center><img src="static/img/readme.png" width="100%"></center>

According to the picture, when a message is sent from the `mahdi` user, the message is sent to the server through websocket.
The server saves the message once in the database and sends the same message again to the mahdi user and other users without the need for a request.
All messages are received in the form of json through the client, and the main part of designing and displaying the messages is the responsibility of the client.

<hr>



## Performance

> [!NOTE]
> It is better to use the **virtualenvironment** when installing libraries and running the project. 

`django channels` is designed in the form of a messenger application whose client is javascript and its back-end has created a websocket-based connection with django.


> [!WARNING]
> Have **redis** installed on the system before running
> download and install [redis for windows](https://github.com/tporadowski/redis/releases) and to `cmd` type `redis-server` to run the redis.

**To install required libraries:**
```
pip install -r requirements.txt
```

**To Run The Project:**
```
python manage.py runserver
```