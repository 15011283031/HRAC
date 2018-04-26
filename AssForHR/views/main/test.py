# -*- coding:utf-8 -*-
#!/usr/bin/env python

import sys


#需要首先配置django的默认app以及设置
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] ='HRA.settings'
django.setup()
from AssForHR import models
import datetime

import MySQLdb



name = '11117110720'
checkout = models.check_out.objects.all()
#checkout = models.check_out.objects.filter(emplid=name).all()
print("人力资源中心")

from AssForHR.views.main.checktime import mysql_con, db_connect

sqlstr = 'select * from AssForHR_check_out where id = 11'
data = mysql_con(sqlstr, db_connect)
print(data[0][1])

print("人力资源中心")






# list_to_insert = []
# for i in check_out_data:
#     list_to_insert.append(models.check_out(department=i[1], emplid=i[2], name=i[3], date=i[4], time=i[5], check_time=i[6], machineid=i[7]))
# models.check_out.objects.bulk_create(list_to_insert)
# for i in list_to_insert:
#     print(i)
