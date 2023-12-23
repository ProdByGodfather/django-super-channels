from django.utils.safestring import mark_safe
import json


def return_username(request):
    username = request.user.username
    context = {
        'username': mark_safe(json.dumps(username)),
        'just_username': username,
    }
    return context