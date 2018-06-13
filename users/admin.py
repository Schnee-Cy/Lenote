from django.contrib import admin
# Register your models here.
from users.models import UserInfo, Message

admin.site.register(UserInfo)
admin.site.register(Message)
