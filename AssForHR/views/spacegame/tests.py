#!/usr/bin/env python
# -*- coding:utf-8 -*-

#需要首先配置django的默认app以及设置
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] ='HRA.settings'
django.setup()
from AssForHR import models


def building_model_add(new_building_model, building_models):
    i = 0
    for building_model in building_models:
        if building_model.building_model_id == new_building_model['building_model_id']:
            i += 1
        else:
            pass
    if i > 0:
        pass
    else:
        models.building_model.objects.create(**new_building_model)


def public_config_group_add(new_group, public_config_groups):
    i = 0
    for group in public_config_groups:
        if group.group_id == new_group['group_id']:
            i += 1
        else:
            pass
    if i > 0:
        pass
    else:
        models.public_config_group.objects.create(**new_group)


def public_config_code_add(new_item, public_config_codes):
    i = 0
    for item in public_config_codes:
        if item.item_id == new_item['item_id']:
            i += 1
        else:
            pass
    if i > 0:
        pass
    else:
        models.public_config_code.objects.create(**new_item)


def player_add(new_player, players):
    i = 0
    for player in players:
        # print('player.PlayerID:%s' % player.PlayerID)
        # print('new_player[PlayerID]:%s' % new_player['PlayerID'])
        if player.PlayerID == new_player['PlayerID']:
            i += 1
        else:
            pass
    # print('i:%s' % i)
    if i > 0:
        pass
    else:
        models.PlayerLists.objects.create(**new_player)


def star_add(new_star, stars):
    i = 0
    for star in stars:
        # print('star.starid:%s' % star.starid)
        # print('new_star[starid]:%s' % new_star['starid'])
        if star.starid == new_star['starid']:
            i += 1
        else:
            pass
    if i > 0:
        pass
    else:
        models.starlists.objects.create(**new_star)


def area_add(new_area, areas):
    i = 0
    for area in areas:
        # print('area.areaid:%s' % area.areaid)
        # print('new_area[areaid]:%s' % new_area['areaid'])
        if area.areaid == new_area['areaid']:
            i += 1
        else:
            pass
    if i > 0:
        pass
    else:
        models.AreaLists.objects.create(**new_area)


def building_add(new_building, buildings):
    i = 0
    for building in buildings:
        # print('building.BuildingID:%s' % building.BuildingID)
        # print('new_building[BuildingID]:%s' % new_building['BuildingID'])
        if building.BuildingID == new_building['BuildingID']:
            i += 1
        else:
            pass
    if i > 0:
        pass
    else:
        models.BuildingLists.objects.create(**new_building)


public_config_groups = models.public_config_group.objects.all()
new_group = {'group_id': '1', 'group_name': 'BuildingStatus', 'order_id': '1'}
public_config_group_add(new_group, public_config_groups)
public_config_groups = models.public_config_group.objects.all()
[print(i) for i in public_config_groups]


public_config_codes = models.public_config_code.objects.all()
new_item_group = models.public_config_group.objects.get(group_id='1')
new_item = {'item_id': '1_1', 'item_name': 'PrepareBuild', 'item_value': '1', 'order_id': 1, 'group_id': new_item_group}
public_config_code_add(new_item, public_config_codes)
new_item = {'item_id': '1_2', 'item_name': 'Building', 'item_value': '2', 'order_id': 2, 'group_id': new_item_group}
public_config_code_add(new_item, public_config_codes)
new_item = {'item_id': '1_3', 'item_name': 'NoUse', 'item_value': '3', 'order_id': 3, 'group_id': new_item_group}
public_config_code_add(new_item, public_config_codes)
new_item = {'item_id': '1_4', 'item_name': 'Using', 'item_value': '4', 'order_id': 4, 'group_id': new_item_group}
public_config_code_add(new_item, public_config_codes)
new_item = {'item_id': '1_5', 'item_name': 'Damaged', 'item_value': '5', 'order_id': 5, 'group_id': new_item_group}
public_config_code_add(new_item, public_config_codes)
new_item = {'item_id': '1_6', 'item_name': 'NeedRepair', 'item_value': '6', 'order_id': 6, 'group_id': new_item_group}
public_config_code_add(new_item, public_config_codes)
public_config_codes = models.public_config_code.objects.all()
[print(i) for i in public_config_codes]



building_models = models.building_model.objects.all()
new_building_model = {'building_model_id': '1', 'building_model_name': 'Nuclear power generator'
    , 'building_type': 'function', 'building_descr': 'projuect energy', 'building_path': '/image/building1.png'
    , 'work_hours': 400, 'max_worker_num': 10, 'product_type': 'energy', 'production_num': 40}
building_model_add(new_building_model, building_models)
building_models = models.building_model.objects.all()
[print(i) for i in building_models]


players = models.PlayerLists.objects.all()
new_player = {'PlayerID': '2', 'Name': 'TestPlayer'}
player_add(new_player, players)
players = models.PlayerLists.objects.all()
[print(i) for i in players]


stars = models.starlists.objects.all()
star_add({'starid': '1', 'star_name': 'TestStar1', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '2', 'star_name': 'TestStar2', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '3', 'star_name': 'TestStar3', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '4', 'star_name': 'TestStar4', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '5', 'star_name': 'TestStar5', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '6', 'star_name': 'TestStar6', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '7', 'star_name': 'TestStar7', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '8', 'star_name': 'TestStar8', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '9', 'star_name': 'TestStar9', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
star_add({'starid': '10', 'star_name': 'TestStar10', 'loc_x': '15', 'loc_y': '14', 'loc_z': '13'}
         , stars)
stars = models.starlists.objects.all()
[print(i) for i in stars]


areas = models.AreaLists.objects.all()
new_area_star = models.starlists.objects.get(starid='2')
area_add({'areaid': '24', 'area_name': 'TestArea24', 'loc_star': new_area_star
    , 'loc_x': '14', 'loc_y': '13', 'loc_z': '13'}, areas)
areas = models.AreaLists.objects.all()
[print(i) for i in areas]


buildings = models.BuildingLists.objects.all()
new_building_player = models.PlayerLists.objects.get(PlayerID='2')
new_building_area = models.AreaLists.objects.get(areaid='24')
new_building_model = models.building_model.objects.get(building_model_id='1')
print(new_building_model)
new_building = {'BuildingID': '1', 'OwnerID': '2', 'building_status_id': '1_2'
    , 'PlayerID': new_building_player
    , 'areaid': new_building_area, 'building_model_id': new_building_model
                , 'now_worker_num': 0, 'now_production_num': 0}
building_add(new_building, buildings)
buildings = models.BuildingLists.objects.all()
[print(i) for i in buildings]








# django.core.exceptions.FieldError: Cannot resolve keyword 'PlayerLists'
# into field. Choices are: BuildingID, BuildingStatusID, OwnerID, PlayerID, PlayerID_id, id



#models.PlayerLists.objects.filter(PlayerID='2').delete()
#models.BuildingLists.objects.filter(BuildingID=new_building['BuildingID']).delete()

