from django.db import models
from django.db import transaction
from goods.models import Goods
from django.db.models import F
from time import sleep

class OrdersManager(models.Manager):
    def add(self,data):
        #with transaction.atomic():
        goods_id = data['goods_id']
        goods_num = data['goods_num']
        row = Goods.objects.filter(pk=goods_id,goods_num__gte=goods_num).update(goods_num=F('goods_num')-goods_num) 
        if row < 1:  
            raise ValueError('库存不足')
        sleep(6)
        return self.create(**data)
class Orders(models.Model):
    order_no = models.BigIntegerField(default=0)
    order_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    goods_id = models.IntegerField(default=0)
    goods_num = models.IntegerField(default=0)
    
    objects = OrdersManager()
    class Meta:
        db_table = 'orders'
        
        
            