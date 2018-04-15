#!/usr/bin/env python
# -*- coding:utf-8 -*-

#需要首先配置django的默认app以及设置
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] ='HRA.settings'
django.setup()

from AssForHR import models


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
new_building = {'BuildingID': '1', 'OwnerID': '2', 'BuildingStatusID': '1', 'PlayerID': new_building_player, 'areaid': new_building_area}
building_add(new_building, buildings)
buildings = models.BuildingLists.objects.all()
[print(i) for i in buildings]






# django.core.exceptions.FieldError: Cannot resolve keyword 'PlayerLists'
# into field. Choices are: BuildingID, BuildingStatusID, OwnerID, PlayerID, PlayerID_id, id



#models.PlayerLists.objects.filter(PlayerID='2').delete()
#models.BuildingLists.objects.filter(BuildingID=new_building['BuildingID']).delete()

