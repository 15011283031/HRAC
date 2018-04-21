# -*- coding: utf-8 -*-
from django.db import models


def decode(info):
    return info.decode('utf-8')


"""
生成数据库的操作：
    1.shell切换到web站点根目录下cd /home/peter/work/HRAC
    2.执行python manage.py makemigrations # 生成配置文件
    3.python manage.py migrate       # 根据配置文件创建数据库相关
注意：
    如果遇到无法导入django的情况，请重新配置系统path到目前项目在用的envs的bin目录下    

"""

# Create your models here.


class EX_SourceSetting(models.Model):
    model_name = models.CharField(max_length=40)
    source_table_name = models.CharField(max_length=40)
    source_col_name = models.CharField(max_length=40)
    source_version_name = models.CharField(max_length=40)

    def __str__(self):
        return '<%s %s>' % (self.model_name, self.source_table_name)


class starlists(models.Model):
    starid = models.CharField(max_length=40, unique=True)
    star_name = models.CharField(max_length=200)
    loc_x = models.IntegerField(default=0)
    loc_y = models.IntegerField(default=0)
    loc_z = models.IntegerField(default=0)

    def __str__(self):
        return '{starid:%s | star_name:%s}' % (self.starid, self.star_name)


class AreaLists(models.Model):
    areaid = models.CharField(max_length=40, unique=True)
    area_name = models.CharField(max_length=200)
    loc_x = models.IntegerField(default=0)
    loc_y = models.IntegerField(default=0)
    loc_z = models.IntegerField(default=0)
    loc_star = models.ForeignKey(to="starlists", to_field='starid'
                                 , on_delete=models.CASCADE, default='0')

    def __str__(self):
        return '{areaid:%s | area_name:%s| loc_star:%s| loc_x:%s| loc_y:%s| loc_z:%s}' \
               % (self.areaid, self.area_name, self.loc_star, self.loc_x, self.loc_y, self.loc_z)


class building_model(models.Model):
    building_model_id = models.CharField(max_length=40, unique=True, default='0')
    building_model_name = models.CharField(max_length=200, default='undifined2')
    building_type = models.CharField(max_length=40)
    building_desc = models.TextField()
    building_path = models.CharField(max_length=400)
    work_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    max_worker_num = models.IntegerField(default=0)
    product_type = models.CharField(max_length=40)
    production_num = models.BigIntegerField(default=0)

    def __str__(self):
        return '{building_model_id:%s | building_model_name:%s| building_type:%s| building_desc:%s' \
               '| building_path:%s| work_hours:%s| max_worker_num:%s| product_type:%s| production_num:%s}' \
               % (self.building_model_id, self.building_model_name, self.building_type, self.building_desc
                  , self.building_path, self.work_hours, self.max_worker_num, self.product_type, self.production_num)


class public_config_group(models.Model):
    group_id = models.CharField(max_length=40, unique=True, default='0')
    group_name = models.CharField(max_length=200, default='undifined')
    order_id = models.IntegerField(default=0)

    def __str__(self):
        return '{group_id:%s | group_name:%s}' % (self.group_id, self.group_name)


class public_config_code(models.Model):
    item_id = models.CharField(max_length=40, default='0_0')
    item_name = models.CharField(max_length=200, default='undifined')
    item_value = models.CharField(max_length=200, default='undifined')
    order_id = models.IntegerField(default=0)
    group_id = models.ForeignKey(to="public_config_group", to_field='group_id'
        , on_delete=models.CASCADE, default='0')

    def __str__(self):
        return '{item_id:%s | item_name:%s| item_value:%s| group_id:%s}' \
               % (self.item_id, self.item_name, self.item_value, self.group_id)


class BuildingLists(models.Model):
    BuildingID = models.CharField(max_length=40, default='0')
    OwnerID = models.CharField(max_length=200, default='undifined')
    building_status_id = models.CharField(max_length=200, default='undifined')
    PlayerID = models.ForeignKey(to="PlayerLists", to_field='PlayerID'
                                 , on_delete=models.CASCADE, default='0')
    areaid = models.ForeignKey(to="AreaLists", to_field='areaid'
                               , on_delete=models.CASCADE, default='0')
    building_model_id = models.ForeignKey(to="building_model", to_field='building_model_id'
        , on_delete=models.CASCADE, default='0')
    now_worker_num = models.IntegerField(default=0)
    now_production_num = models.BigIntegerField(default=0)
    now_work_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return '{BuildingID:%s | OwnerID:%s| building_status_id:%s' \
               '| now_worker_num:%s| now_production_num:%s| now_work_hours:%s' \
               '| PlayerID:%s| areaid:%s| building_model_id:%s}' \
               % (self.BuildingID, self.OwnerID, self.building_status_id
                  , self.now_worker_num, self.now_production_num, self.now_work_hours
                  , self.PlayerID, self.areaid, self.building_model_id)


class PlayerLists(models.Model):
    PlayerID = models.CharField(max_length=40, default='0', unique=True, null=False)
    Name = models.CharField(max_length=200, default='undifined')
    CreateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{PlayerID:%s | Name:%s}' % (self.PlayerID, self.Name)


class BuildingsView(models.Model):
    class Meta:
         managed = False
         db_table = "AssForHR_buildings_view"

