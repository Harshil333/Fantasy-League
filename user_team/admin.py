from django.contrib import admin
from user_team.models import UserPlayer,UserTeam

# Register your models here.
# class UserPlayerInline(admin.TabularInline):
#     model = UserPlayer
# admin.site.register(UserTeam)
#admin.site.register(UserPlayer)
admin.site.register(UserPlayer)
admin.site.register(UserTeam)