from django.contrib import admin
from .models import Action, Prompt, User

# Register your models here.

admin.site.register(Action)
admin.site.register(Prompt)
admin.site.register(User)
