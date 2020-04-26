from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'fantasy_app'

urlpatterns = [
    url(r'^teamdetail/(?P<slug>[-\w]+)/$',views.TeamDetailView.as_view(),name='team_detail'),
    url(r'^playerdetail/(?P<slug>[-\w]+)/$',views.PlayerDetailView.as_view(),name='player_detail'),
    url(r'^playerlist/$',views.PlayerListView.as_view(),name='player_list'),
    url(r'^matchlist/$',views.MatchListView.as_view(),name='match_list'),
    url(r'^teamlist/$',views.TeamListView.as_view(),name='teamlist'),
    url(r'^teamdetail/(?P<slug>[-\w]+)/$', views.TeamDetailView.as_view(), name='singleteam'),
]