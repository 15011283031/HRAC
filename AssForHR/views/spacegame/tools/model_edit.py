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
        models.BuildingLists.objects.filter(BuildingID=new_building['BuildingID']).delete()
        models.BuildingLists.objects.create(**new_building)
    else:
        models.BuildingLists.objects.create(**new_building)

