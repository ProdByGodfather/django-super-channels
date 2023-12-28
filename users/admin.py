from django.contrib import admin
from users import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email','is_superuser')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('last_login','is_superuser')



admin.site.register(models.User,UserAdmin)