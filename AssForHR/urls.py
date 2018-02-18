from django.conf.urls import url
from AssForHR.views.main import main, updateLogin, updateWebSource
from AssForHR.views.exchange import exchangeSetting


urlpatterns = [
    url(r'^$', main.main, name='main'),
    url(r'^updateLogin$', updateLogin.loginConfig, name='loginConfig'),
    url(r'^saveNewConnecttion/$', updateLogin.saveNewConnecttion, name='saveNewConnecttion'),
    url(r'^updateWebSource$', updateWebSource.websourceConfig, name='websourceConfig'),
    url(r'^saveWebSource/$', updateWebSource.saveWebSource, name='saveWebSource'),
    url(r'^main/$', main.main, name='main'),
    url(r'^exchangeSetting/$', exchangeSetting.exchangeSettingLogin, name='exchangeSettingLogin'),
]