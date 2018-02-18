from django.db import models

# Create your models here.
class EX_SourceSetting(models.Model):
    model_name = models.CharField(max_length=40)
    source_table_name = models.CharField(max_length=40)
    source_col_name = models.CharField(max_length=40)
    source_version_name = models.CharField(max_length=40)

