from __future__ import unicode_literals

from django.db import models, connection
from django.template.defaultfilters import default
from django.contrib.auth.models import User

# Create your models here.

class configuration(models.Model):
    config=models.CharField(max_length=100)
    status=models.CharField(max_length=30,default="pending")
    
    def truncat(self):
        cursor=connection.cursor()
        table_name = self.model._meta.db_table
        sql = "TRUNCATE TABLE %s;" % (table_name, )
        cursor.execute(sql)
    
    def __str__(self):
        return self.config
   
    
class post(models.Model):
    host_name=models.CharField(max_length=100)
    usrname=models.CharField(max_length=30)
    passwd=models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return self.host_name
 
        
class srcdest(models.Model):
    source=models.CharField(max_length=1000)
    destination=models.CharField(max_length=1000)

    def __str__(self):
        return self.source