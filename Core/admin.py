from django.contrib import admin
from .models import Message
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "time_stamp")


admin.site.register(Message, MessageAdmin)

