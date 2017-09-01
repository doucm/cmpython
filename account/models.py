from django.db import models

import logging
logger = logging.getLogger('cmsys')

class AccountManager(models.Manager):
    logger.info('init')
    def add(self, *args, **kwargs):
        logger.info('create')
        self.create(**kwargs)
        AccountLogs.objects.create(msg='account')
        
class BaseAccount(models.Model):
    money = models.BigIntegerField(default=0)
    
    class Meta:
        abstract=True
        
class Account(BaseAccount):
    
    objects = AccountManager()
    
    class Meta:
        db_table='account'
        
class AccountTrigger(BaseAccount):
    class Meta:
        db_table='account_trigger'
        
class AccountLogs(models.Model):
    msg = models.CharField(max_length=50)
    class Meta:
        db_table='account_logs'