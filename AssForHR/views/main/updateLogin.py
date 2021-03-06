# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response

# 用于加密算法
import AssForHR.views.main.tools.prpcrypt as prpcrypt

# 调用加密算法，用于加密数据库链接中的密码
from AssForHR.views.main.tools.randomstring import randomstring
# JSON数据格式
import json  # json数据格式，用于写入数据库链接配置信息

import os  # 用于检测文件目录是否存在

# from django.http import JsonResponse
from django.http import HttpResponseRedirect

# 设置随机字符串 默认被 saveNewConnecttion 调用


class DBSource:
    '''default dbsource
        properties:servername,dbusername,dbpsw,dbname
        setters:setServername(servername),setDbusername(dbusername),setDbpsw(dbpsw),setDbname(dbname)
        getters:getServername(),getDbusername(),getDbpsw(),getDbname()
        match(DBSource)
    '''
    def __init__(self,servername,dbusername,dbpsw,dbname):
        self.servername = servername
        self.dbusername = dbusername
        self.dbpsw = dbpsw
        self.dbname = dbname

    def setServername(self,servername):
        self.servername = servername

    def setDbusername(self,dbusername):
        self.dbusername = dbusername    

    def setDbpsw(self,dbpsw):
        self.dbpsw = dbpsw    

    def setDbname(self,dbname):
        self.dbname = dbname

    def getServername(self):
        return self.servername

    def getDbusername(self):
        return self.dbusername

    def getDbpsw(self):
        return self.dbpsw   

    def getDbname(self):
        return self.dbname  

    def match(self,DBSource):
        if self.servername == DBSource.servername and self.dbusername == DBSource.dbusername and self.dbpsw == DBSource.dbpsw and self.dbname == DBSource.dbname:
            return True
        else:
            return False 

    def getInfo(self):
        return '<br>Servername:%s;<br>Dbname:%s;<br>Dbusername:%s;'%(self.servername,self.dbname,self.dbusername)           


def readConn():
    # readConn from sourcename.json
    dbConn = DBSource(r'peter', r'sa', r'111111', r'gaia')
    if os.path.exists('./AssForHR/static/config/sourcename.json'):
        if os.path.getsize('./AssForHR/static/config/sourcename.json'):
            with open('./AssForHR/static/config/sourcename.json') as connFile:
                readConnDict = json.load(connFile)
                decrypt_tmpkey = prpcrypt.prpcrypt(readConnDict['dbsalt'])
                decrypt_psw = decrypt_tmpkey.decrypt(readConnDict['dbpsw'])
                dbConn = DBSource(readConnDict['servername'],readConnDict['dbusername'],decrypt_psw,readConnDict['dbname'])
    return dbConn


# 配置新链接
def saveNewConnecttion(request):
    ''' get website post:servername,dbusername,dbpsw,dbname,sourcename
        write to sourcename.json:servername,dbusername,dbpsw,dbname,sourcename,dbsalt
        return result ['Success','Failed']
    '''
    if request.method == "POST": 
        connInfo=dict()              
        connInfo['servername'] =  request.POST.get('servername')
        connInfo['dbusername'] = request.POST.get('dbusername')
        tempsw = request.POST.get('dbpsw')
        connInfo['dbname'] = request.POST.get('dbname')
        connInfo['sourcename'] = request.POST.get('sourcename')
        
        tempkey = randomstring(16)
        pc = prpcrypt.prpcrypt(tempkey)
        encryptedKey = pc.encrypt(tempsw)
        connInfo['dbpsw'] = str(encryptedKey.decode())
        connInfo['dbsalt'] = str(tempkey)
        
        tmpehr = DBSource(connInfo.get('servername'),connInfo.get('dbusername'),tempsw,connInfo.get('dbname'))
    
        with open('./AssForHR/static/config/sourcename.json','w+') as file_object:
            json.dump(connInfo,file_object)
    
        ehr = readConn()
        dbSourceInfo = readConn().getInfo() 
        if tmpehr.match(ehr):       
            return HttpResponseRedirect("/AssForHR")
    return HttpResponse(dbSourceInfo)


def loginConfig(request):
    '''request for updateLogin '''
    return render_to_response('AssForHR/updateLogin.html')

