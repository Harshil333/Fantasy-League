from django.conf.urls import url
from . import views
from fantasy_app import views as v1
from django.urls import path
app_name = 'user_team'

urlpatterns = [
    path('viewmyteam/',views.UserPlayerListView.as_view(),name='viewmyteam'),
    url(r'^create/',v1.PlayerListView.as_view(template_name='user_team/create_team.html'),name='create'),
    url(r'^add/(?P<slug>[-\w]+)/$',views.AddToTeam.as_view(),name='add'),
    url(r'^remove/(?P<slug>[-\w]+)/$',views.RemoveFromTeam.as_view(),name='remove'),
    url(r'^leaderboard/', views.LeaderBoard.as_view(), name='leaderboard'),
]  