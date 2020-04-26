from django.shortcuts import render
from django.views import generic
from fantasy_app.models import Team,Player,Match
from user_team.models import UserTeam,UserPlayer
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class TeamDetailView(generic.DetailView):
    model = Team

    # def get_context_data(self,**kwargs):
    #     context = super(TeamDetailView, sekf).get_context_data(**kwargs)
    #     player_list = [player for player in Player.objects.filter(team=)]

class TeamListView(generic.ListView):
    model = Team
    
class PlayerDetailView(generic.DetailView):
    model = Player

class PlayerListView(generic.ListView):
    model = Player

    context_object_name = 'player_list'
    template_name = 'user_team/create_team.html'
    # queryset = Player.objects.all()

    def get_context_data(self,**kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        user=self.request.user
        userplayer_list = [user.player for user in UserPlayer.objects.filter(user=user)]
        credits=10
        for i in userplayer_list:
            credits-=i.credit
        print("Credits:",credits)
        context['credits'] = credits
        context['isValid'] = True
        context['userplayer_list'] = userplayer_list
        return context

class MatchListView(generic.ListView):
    model = Match

    def get_queryset(self):
        return Match.objects.filter(date__gte=timezone.now()).order_by(-date)
