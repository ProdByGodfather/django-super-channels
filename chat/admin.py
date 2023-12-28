from django.contrib import admin
from chat import models

class ChatAdmin(admin.ModelAdmin):
    list_display = ('roomname','createtime')
    search_fields = ("roomname",)
    list_filter = ('createtime',)
    date_hierarchy = 'createtime'


class RoomAdmin(admin.ModelAdmin):
    list_display = ('author','timestamp','related_chat')
    list_filter = ('timestamp',)
    search_fields = ('author',)
    date_hierarchy = 'timestamp'

# Register The models here.
admin.site.register(models.Chat,ChatAdmin)
admin.site.register(models.Message,RoomAdmin)