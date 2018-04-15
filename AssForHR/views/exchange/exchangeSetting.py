from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from suds.client import Client
import http.cookiejar as cookielib
#from AssForHR import models



def exchangeSettingLogin(request):
    '''request for exchangeSetting '''
    # dic_insertdata = {
    #     "model_name": '员工信息'
    #     , "source_table_name": 'PeopleSoft生产'
    #     , "source_col_name": '姓名'
    #     , "source_version_name": '1.0.0.0'}
    # models.EX_SourceSetting.objects.create(**dic_insertdata)

    #ex_SourceSetting = models.EX_SourceSetting.objects.all()
    for sin_EX_SourceSetting in ex_SourceSetting:
        print("模组名称：%s；数据源名称：%s；列名：%s；版本号：%s；" % (sin_EX_SourceSetting.model_name
                                                  , sin_EX_SourceSetting.source_table_name
                                                  , sin_EX_SourceSetting.source_col_name
                                                  , sin_EX_SourceSetting.source_version_name))
    #return render_to_response('./exchangeData/exchangeSetting.html')
    return render(request, './exchangeData/exchangeSetting.html', {'ex_SourceSetting': ex_SourceSetting})
    #return  HttpResponse('ok')