from django.conf.urls import url
from . import views

app_name = 'games'

urlpatterns = [
    # /games/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /games/register/
    url(r'register/$', views.UserFormView.as_view(), name='register'),


    # /games/all_games/
    url(r'all_games/$', views.AllGames.as_view(), name='all_games'),


    # /games/<console_id>/ #
    url(r'^(?P<pk>[0-9]+)$', views.ConsoleGames.as_view(), name='console_games'),

    # /games/console/add/ #
    url(r'console/add/$', views.ConsoleCreate.as_view(), name='console_add'),

    # /games/console/<pk>/ #
    url(r'console/(?P<pk>[0-9]+)/$', views.ConsoleUpdate.as_view(), name='console_update'),

    # /games/console/<pk>/delete #
    url(r'console/(?P<pk>[0-9]+)/delete/$', views.ConsoleDelete.as_view(), name='console_delete'),

    # /games/<game_id>/ #
    url(r'^(?P<pk>[0-9]+)/$', views.GameDetail.as_view(), name='game_detail'),

    # /games/game/add/ #
    url(r'game/add/$', views.GameCreate.as_view(), name='game_add'),

    # /games/console/<pk>/ #
    url(r'game/(?P<pk>[0-9]+)/$', views.GameUpdate.as_view(), name='game_update'),

    # /games/game/<pk>/delete #
    url(r'game/(?P<pk>[0-9]+)/delete/$', views.GameDelete.as_view(), name='game_delete'),

    # /games/<game_id>/completed/ #
    #url(r'^(?P<game_id>[0-9]+)/completed/$', views.completed, name='completed'),
]
