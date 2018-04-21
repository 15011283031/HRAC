import os
os.environ['DJANGO_SETTINGS_MODULE']= 'HRA.settings'
import django
django.setup()
from django.shortcuts import render_to_response
from django.shortcuts import render
from AssForHR import models


def get_building_status_desc(building_status_id):
    building_status_desc = models.public_config_code.objects.get(item_id=building_status_id).item_name
    return building_status_desc


def main(request):
    '''request for updateLogin '''
    return render_to_response('spacegame/spacegameindex.html')


def movetostar(request):
    ''' 进入星球管理页面，可以显示每个人账户下星球 '''
    round = 1
    starlists = models.starlists.objects.all()
    print(type(starlists))
    context = {'starlists': starlists, 'round': round}
    return render(request, 'spacegame/starmanage.html', context)


def star_overview_all(request, starid):
    """
    星球总览页面，查看全部总览信息，能够看到星球下总体状态
    """
    print(starid)
    context = {'starid': starid}
    return render(request, 'spacegame/star_overview_all.html', context)


def area_edit(request, starid, areaid, panelid):
    """
    区域编辑页面，编辑区域：进行建造、安排等工作
    """
    # building
    print('starid:%s' % starid)
    print('areaid:%s' % areaid)
    print('areaid:%s' % panelid)
    building = models.BuildingLists.objects.get(OwnerID=2, areaid=24)
    print('building:%s' % building)
    print('building_status_id:%s' % building.building_status_id)
    building_status = get_building_status_desc(building.building_status_id)
    print('building_status:%s' % building_status)
    context = {'starid': id, 'areaid': areaid, 'panelid': panelid, 'building': building
        , 'building_status': building_status}
    return render(request, 'spacegame/area_edit.html', context)
