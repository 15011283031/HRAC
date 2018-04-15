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
        return '||starid:%s | star_name:%s||' % (self.starid, self.star_name)


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


class Building_Model(models.Model):
    buildingID = models.CharField(max_length=40)
    buildingName = models.CharField(max_length=200, default='undifined2')
    buildingType = models.CharField(max_length=40)
    buildingDescr = models.TextField()
    buildingPath = models.CharField(max_length=400)
    workHours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    maxWorkerNum = models.IntegerField(default=0)
    productType = models.CharField(max_length=40)
    productionNum = models.BigIntegerField(default=0)

    def __str__(self):
        return '||buildingID:%s | buildingName:%s||' % (self.buildingID, self.buildingName)


class PublicConfigGroup(models.Model):
    GroupID = models.CharField(max_length=40, default='0_0')
    GroupName = models.CharField(max_length=200, default='undifined')
    OrderID = models.IntegerField(default=0)

    def __str__(self):
        return '||GroupID:%s | GroupName:%s||' % (self.GroupID, self.GroupName)


class PublicConfigCode(models.Model):
    ItemID = models.CharField(max_length=40, default='0_0')
    ItemName = models.CharField(max_length=200, default='undifined')
    ItemValue = models.CharField(max_length=200, default='undifined')
    OrderID = models.IntegerField(default=0)
    GroupID = models.CharField(max_length=40, default='0_0')

    def __str__(self):
        return '||ItemID:%s | ItemName:%s||' % (self.ItemID, self.ItemName)


class BuildingLists(models.Model):
    BuildingID = models.CharField(max_length=40, default='0')
    OwnerID = models.CharField(max_length=200, default='undifined')
    BuildingStatusID = models.CharField(max_length=200, default='undifined')
    PlayerID = models.ForeignKey(to="PlayerLists", to_field='PlayerID'
                                 , on_delete=models.CASCADE, default='0')
    areaid = models.ForeignKey(to="AreaLists", to_field='areaid'
                               , on_delete=models.CASCADE, default='0')

    def __str__(self):
        return '{BuildingID:%s | OwnerID:%s| BuildingStatusID:%s| PlayerID:%s| areaid:%s}' \
               % (self.BuildingID, self.OwnerID, self.BuildingStatusID, self.PlayerID, self.areaid)


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

