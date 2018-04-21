from django import forms # 从django导入forms


# 新建form表单类，用于操作表单
class _MainBuilding(forms.Form):
    building_model_id = forms.CharField(max_length=40)

