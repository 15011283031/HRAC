import os
os.environ['DJANGO_SETTINGS_MODULE']= 'HRA.settings'
import django
django.setup()
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from AssForHR import models
import MySQLdb
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json #json数据格式，用于写入数据库链接配置信息


class Db_connnect():
    def __init__(self, host, user_name, psw, db_name):
        self.host = host
        self.user_name = user_name
        self.psw = psw
        self.db_name = db_name


db_connect = Db_connnect("localhost", "root", "", "assforgaia")


def mysql_con(sql_str, db_connect):
    # 打开数据库连接
    db = MySQLdb.connect(db_connect.host, db_connect.user_name, db_connect.psw, db_connect.db_name, charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute(sql_str)

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()

    # 关闭数据库连接
    db.commit()
    db.close()


    return data


def update_syn_log(syn_result, syn_item, state, db_connect):
    syn_data = read_syn_log(syn_item, db_connect)
    # print('len syn_data:%s' % len(syn_data))
    if len(syn_data) > 0:
        sql_str = "update syn_record set syn_time = now(), syn_result = " + syn_result + ", syn_item = " + syn_item + "" \
                  ",state = " + state + ",operator = 'sa' where syn_item = " + syn_item + ";"
        # print('update sql_str:%s' % sql_str)
    else:
        sql_str = "insert into syn_record (syn_time,syn_result,syn_item,state,operator)" \
                  "values (now(), "+syn_result+", "+syn_item+", "+state+", 'sa')"
        # print('insert sql_str:%s' % sql_str)
    mysql_con(sql_str, db_connect)


def read_syn_log(syn_item, db_connect):
    sql_str = "select syn_time,syn_result,syn_item,state,operator from syn_record " \
              "where syn_item = '"+syn_item+"' limit 1;"
    # print(sql_str)
    syn_data = mysql_con(sql_str, db_connect)
    return syn_data


def check_out_syn():
    syn_data = read_syn_log('1', db_connect)
    if len(syn_data) > 0:
        syn_maxid = syn_data[0][1]
    else:
        syn_maxid = 0
    # print('maxid:%s' % syn_maxid)
    sql_str = "select * from check_record_view "
    check_out_data = mysql_con(sql_str, db_connect)
    max_step = len(check_out_data)
    j = 0
    for i in check_out_data:
        j += 1
        # print('department:%s' % i[1])
        # print('emplid:%s' % i[2])
        # print('name:%s' % i[3])
        # print('date:%s' % i[4])
        # print('time:%s' % i[5])
        # print('check_time:%s' % i[6])
        # print('machineid:%s' % i[7])
        # print('id:%s' % i[0])
        # print('maxid:%s' % syn_maxid)
        # print('max_step:%s' % max_step)
        if i[0] > int(syn_maxid):
            list_to_insert = {}
            list_to_insert['department'] = i[1]
            list_to_insert['emplid'] = i[2]
            list_to_insert['name'] = i[3]
            list_to_insert['date'] = datetime.datetime.strftime(i[6], "%Y-%m-%d")
            list_to_insert['time'] = datetime.datetime.strftime(i[6], "%H:%M:%S")
            list_to_insert['check_time'] = datetime.datetime.strftime(i[6], "%Y-%m-%d %H:%M:%S")
            list_to_insert['machineid'] = i[7]
            models.check_out.objects.create(**list_to_insert)
            syn_num = i[0]
            # print('j:%s;max_step:%s' % (j, max_step))
            if j == max_step:
                # print("update syn log")
                update_syn_log(str(i[0]), '1', '1', db_connect)
        else:
            pass
        #print("chenk out syn ")


def checkout_show(request):
    checkout_lists = models.check_out.objects.all().order_by("department", "emplid", "-check_time")
    # 对部门进行去重
    department_lists = models.check_out.objects.values('department').all()
    department_list = []
    page = ''
    dept_str=''
    for sin_department in department_lists:
        department_list.append(sin_department['department'])
    department_list = list(set(department_list))
    while '' in department_list:
        department_list.remove('')
    print(department_list)

    if request.method == "POST":
        check_out_syn()
        department_name = request.POST.getlist('department_name')
        dept_str = ''
        if len(department_name) > 0:
            for each_dept in department_name:
                dept_str = dept_str + each_dept + ','
            dept_str = dept_str[:len(dept_str)-1]
        print('dept_str:%s' % dept_str)
        employee_id = request.POST.get('employee_id')
        employee_name = request.POST.get('employee_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        page = request.POST.get('now_page')
        if start_date == '':
            start_date = '1990-01-01'
        if end_date == '':
            end_date = '2099-01-01'
        print('department_name:%s' % (type(department_name)))
        print('employee_id:%s' % (employee_id))
        print('employee_name:%s' % (employee_name))
        print('start_date:%s' % (start_date))
        print('end_date:%s' % (end_date))
        print('page:%s' % (page))

        form_values = {}
        form_values['department_name'] = department_name
        form_values['employee_id'] = employee_id
        form_values['employee_name'] = employee_name
        form_values['start_date'] = start_date
        form_values['end_date'] = end_date





        checkout_lists = models.check_out.objects.filter(department__in=department_name
            , emplid__contains=employee_id
            , name__contains=employee_name
            , check_time__gte=datetime.datetime.strptime(start_date, '%Y-%m-%d')
            , check_time__lte=datetime.datetime.strptime(end_date, '%Y-%m-%d')
        ).all().order_by("department", "emplid", "-check_time")
    else:
        pass

    paginator = Paginator(checkout_lists, 20)  # Show 25 contacts per page


    max_page = 6
    min_page = 1

    try:
        checkout_page = paginator.page(page)
        if int(page) > 3:
            min_page = int(page) - 3
        max_page = int(page) + 3
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        checkout_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        checkout_page = paginator.page(paginator.num_pages)
        max_page = paginator.num_pages
        min_page = paginator.num_pages - 6
    if request.method == "POST":
        content = {'checkout_lists': checkout_page, 'check_nums': len(checkout_page)
            , 'form_values': form_values, 'max_page': max_page, 'min_page': min_page
            , 'department_list': department_list, 'dept_str': dept_str}
    else:
        content = {'checkout_lists': checkout_page, 'check_nums': len(checkout_page)
            , 'max_page': max_page, 'min_page': min_page, 'department_list': department_list
            , 'dept_str': dept_str}
    print(content)
    return render(request, 'assforhr/checkout.html', content)

