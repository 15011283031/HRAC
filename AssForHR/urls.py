from django.conf.urls import url
from AssForHR.views.main import main, updateLogin, updateWebSource
from AssForHR.views.exchange import exchangeSetting
from AssForHR.views.spacegame import spacegameindex


urlpatterns = [
    url(r'^$', main.main, name='main'),
    url(r'^updateLogin$', updateLogin.loginConfig, name='loginConfig'),
    url(r'^saveNewConnecttion/$', updateLogin.saveNewConnecttion, name='saveNewConnecttion'),
    url(r'^updateWebSource$', updateWebSource.websourceConfig, name='websourceConfig'),
    url(r'^saveWebSource/$', updateWebSource.saveWebSource, name='saveWebSource'),
    url(r'^main/$', main.main, name='main'),
    url(r'^exchangeSetting/$', exchangeSetting.exchangeSettingLogin, name='exchangeSettingLogin'),
    url(r'^spacegame/$', spacegameindex.main, name='main'),
    url(r'^spacegame/starmanage/(?P<starid>\d+)/$', spacegameindex.star_overview_all),
    url(r'^spacegame/starmanage/$', spacegameindex.movetostar, name='movetostar'),
    url(r'^spacegame/starmanage/(?P<starid>\d+)/(?P<areaid>\d+)/(?P<panelid>\d+)/$', spacegameindex.area_edit),

]