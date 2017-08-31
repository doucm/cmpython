from django.db import models

class Goods(models.Model):
    goods_name = models.CharField(max_length=60)
    goods_num = models.IntegerField()
    
    class Meta:
        db_table = 'goods'