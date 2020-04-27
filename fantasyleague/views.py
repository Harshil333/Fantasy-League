from django.views.generic import TemplateView
from fantasy_app.models import Match,Player
from user_team.models import UserTeam

class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = "index.html"
    def get_context_data(self,**kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['match_list'] = Match.objects.all()
        context['user_team_list'] = UserTeam.objects.all().order_by('-total_points')
        context['best_batsman'] = Player.objects.filter(designation__exact='Bat').order_by('-points')[0]
        context['best_bowler'] = Player.objects.filter(designation__exact='Bowl').order_by('-points')[0]
        context['best_ar'] = Player.objects.filter(designation__exact='All round').order_by('-points')[0]
        return context
