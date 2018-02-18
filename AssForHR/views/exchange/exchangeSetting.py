from django.http import HttpResponse
from django.shortcuts import render_to_response
from suds.client import Client
import http.cookiejar as cookielib

def exchangeSettingLogin(request):
    '''request for exchangeSetting '''
    return render_to_response('./exchangeData/exchangeSetting.html')