import os
os.environ['DJANGO_SETTINGS_MODULE']= 'HRA.settings'
import django
django.setup()
from django.shortcuts import render_to_response
from django.shortcuts import render
from AssForHR import models
from AssForHR.views.spacegame import spacegame_forms
from AssForHR.views.spacegame.tools import model_edit



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
    building = models.BuildingLists.objects.get(OwnerID=2, areaid=areaid)
    print('building:%s' % building)
    print('building_status_id:%s' % building.building_status_id)
    building_status = get_building_status_desc(building.building_status_id)
    print('building_status:%s' % building_status)
    context = {'starid': id, 'areaid': areaid, 'panelid': panelid, 'building': building
        , 'building_status': building_status}
    return render(request, 'spacegame/area_edit.html', context)


def area_main_building_edit(request, starid, areaid, panelid):
    owner_id = '2'
    # main_buliding edit
    print('starid:%s' % starid)
    print('areaid:%s' % areaid)
    print('areaid:%s' % panelid)
    building = models.BuildingLists.objects.get(OwnerID=owner_id, areaid=areaid)
    # print('building:%s' % building)
    # 获取建筑状态（描述）
    building_status = get_building_status_desc(building.building_status_id)
    # 获取建筑物模型列表
    building_models = models.building_model.objects.all()
    # print('building_models:%s' % building_models)

    if request.method == "POST":
        add_building_model_id = request.POST.get('building_model_id')
        # form_data = add_building_model_id.cleaned_data
        building = models.BuildingLists.objects.get(OwnerID=owner_id, areaid=areaid)
        buildinglist = []
        buildinglist.append(building)
        new_building_player = models.PlayerLists.objects.get(PlayerID=owner_id)
        new_building_area = models.AreaLists.objects.get(areaid=areaid)
        new_building_model = models.building_model.objects.get(building_model_id=add_building_model_id)

        new_building = {'BuildingID': building.BuildingID, 'OwnerID': owner_id, 'building_status_id': '1_2'
            , 'PlayerID': new_building_player
            , 'areaid': new_building_area, 'building_model_id': new_building_model
            , 'now_worker_num': 0, 'now_production_num': 0, 'now_work_hours': 0.0}
        # print('post new_building:%s' % new_building)
        model_edit.building_add(new_building, buildinglist)
        building = models.BuildingLists.objects.get(OwnerID=owner_id, areaid=areaid)
        building_status = get_building_status_desc(building.building_status_id)
    else:
        pass
    context = {'starid': id, 'areaid': areaid, 'panelid': panelid, 'building': building
        , 'building_status': building_status, 'building_models': building_models}
    return render(request, 'spacegame/area_main_building_edit.html', context)


def area_add_building_edit(request, starid, areaid, panelid):
    # add_buliding edit
    print('starid:%s' % starid)
    print('areaid:%s' % areaid)
    print('areaid:%s' % panelid)
    context = {'starid': id, 'areaid': areaid, 'panelid': panelid}
    return render(request, 'spacegame/area_add_building_edit.html', context)


def area_main_building_build(request, starid, areaid, panelid):
    # add_buliding edit
    print('starid:%s' % starid)
    print('areaid:%s' % areaid)
    print('areaid:%s' % panelid)
    if request.method == "POST":
        print(request.POST)



    context = {'starid': id, 'areaid': areaid, 'panelid': panelid}
    return render(request, 'spacegame/area_add_building_edit.html', context)