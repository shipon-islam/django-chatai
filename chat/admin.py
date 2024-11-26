from django.contrib import admin
from .models import Messages, Conversation
admin.site.register(Conversation)
admin.site.register(Messages)

# Register your models here.
