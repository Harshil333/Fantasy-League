from django.contrib import admin
from fantasy_app.models import Team,Player,Match
# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)