"""gw2_webclient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from gw2 import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^accounts/profile/$', views.homepage, name='homepage'),
    url(r'^dailies/$', views.getDailyAchievement, name='dailies'),
    url(r'^professions/$', views.getInfoProfession, name='professions'),
    url(r'^professions/(?P<prof_id>.*)/training/$', views.getTraining, name='training'),
    url(r'^professions/(?P<prof_id>.*)/skills/$', views.getProfessionSkills, name='professionskills'),
    url(r'^professions/(?P<prof_id>.*)/weapons/$', views.getWeapons, name='weapons'),
    url(r'^tradingpost/$', views.tradingPost, name='trading_post'),
    url(r'^tradingpost/current/$', views.getTradingPostCurrent, name='trading_post_current'),
    url(r'^tradingpost/history/$', views.getTradingPostHistory, name='trading_post_history'),
    url(r'^events/$', views.getEvents, name='events'),
    url(r'^bank/$', views.getBank, name='bank'),
    url(r'^characters/$', views.getCharacterList, name='characters'),
    url(r'^characters/info/$', views.getCharacterInfo, name='characterinfo'),
    url(r'^characters/inventory/$', views.getInventory, name='inventory'),
    url(r'^characters/stats/$', views.getGear, name='gear'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^registration/register/$', views.register, name='register'),
    url(r'^pvp/$', views.pvp, name='pvp'),
    url(r'^pvp/stats/$', views.getPvPStats, name='pvp_stats'),
    url(r'^pvp/games/$', views.getPvPGames, name='pvp_games'),
    url(r'^admin/', admin.site.urls),
]