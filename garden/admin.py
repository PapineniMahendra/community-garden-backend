from django.contrib import admin
from .models import UserProfile, Event, Participation, Comment

admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Participation)
admin.site.register(Comment)
