from django.contrib import admin
from dashboard.models import AiUser, Position, Candidates, Vote
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group),
admin.site.register(AiUser),
admin.site.register(Position),
admin.site.register(Candidates),
admin.site.register(Vote),