from django.contrib import admin
from dashboard.models import AiUser
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group),
admin.site.register(AiUser),