# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
import json
from AssForHR.views.main import updateWebSource, updateLogin


def main(request):
    '''request for updateWebSource '''
    webSourceInfo = []   
    dbSourceInfo = [] 
    webSourceInfo.append(updateWebSource.classReadWebSouce().getInfo())
    dbSourceInfo.append(updateLogin.readConn().getInfo())
    return render_to_response('./AssForHR/main.html', {
        'webSourceInfo': json.dumps(webSourceInfo),
        'dbSourceInfo': json.dumps(dbSourceInfo)
    })