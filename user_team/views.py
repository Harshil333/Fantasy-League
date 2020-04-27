from django.shortcuts import render
from user_team.models import UserTeam,UserPlayer
from fantasy_app.models import Player
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db import IntegrityError
from django.contrib import messages
from django.urls import reverse
# Create your views here.

class LeaderBoard(generic.ListView):
    model = UserTeam
    template_name = 'user_team/leaderboard.html'
    context_object_name = 'user_team_list'

    def get_queryset(self):
        return UserTeam.objects.all().order_by('-total_points')

class UserPlayerListView(LoginRequiredMixin,generic.ListView):
    model = UserPlayer
    template_name = 'user_team/userplayer_list.html'
    def get_context_data(self,**kwargs):
        context = super(UserPlayerListView, self).get_context_data(**kwargs)
        user=self.request.user
        userplayer_list = [user.player for user in UserPlayer.objects.filter(user=user)]
        points = 0
        for i in userplayer_list:
            points+=i.points
        user_team = UserTeam.objects.get_or_create(user=self.request.user)[0]
        user_team.total_points = points
        user_team.save()
        context['points'] = points
        context['user_team'] = user.username
        return context
    
    
class AddToTeam(LoginRequiredMixin,generic.RedirectView):
    isValid = False
    def get_redirect_url(self, *args, **kwargs):    
        return reverse('user_team:create')
    
    def get(self, request, *args, **kwargs):
        player = get_object_or_404(Player,slug=self.kwargs.get('slug'))
        user=self.request.user
        userplayer_list = [i.player for i in UserPlayer.objects.filter(user=user)]
        try:
            current_player = UserPlayer.objects.create(user=self.request.user,player=player)
        except IntegrityError:
            messages.warning(self.request,'Warning already a member!')
        else:
            messages.success(self.request,'This player is now a member!')
            
        return super().get(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        context['isValid'] = isValid
        return context

class RemoveFromTeam(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('user_team:create')

    def get(self, request, *args, **kwargs):
        try:
            player = UserPlayer.objects.filter(user=self.request.user,player__slug=self.kwargs.get('slug')).get()
        except UserPlayer.DoesNotExist:
            messages.warning(self.request,'Sorry, this player is not in this Team!')
        else:
            player.delete()
            messages.success(self.request,'You removed the player!')
        return super().get(request,*args,**kwargs)  