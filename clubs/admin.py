from django.contrib import admin
from .models import Club, Session, Member, Participant

admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Session)
admin.site.register(Participant)

