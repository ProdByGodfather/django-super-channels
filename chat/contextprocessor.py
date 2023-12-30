from django.utils.safestring import mark_safe
import json


def return_username(request):
    try:
        username = request.user.username
        """
        this function will return 2 atgs
        username returned 'user.username'
        just_username returned user.username
        difference between username and just_username are semicolon
        username for json and just_username for view and if
        """
        context = {
            'username': mark_safe(json.dumps(username)),
            'just_username': username,
        }
        return context
    except:
        context = {
            'username': "ghost user",
            'just_username': "ghost user",
        }
        return context