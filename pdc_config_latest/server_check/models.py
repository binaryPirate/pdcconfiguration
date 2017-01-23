from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default
from django.contrib.auth.models import User
from django.contrib.auth.views import password_change

# Create your models here.
class servers(models.Model):
    servername=models.CharField(max_length=100)
    hostname=models.CharField(max_length=100)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=40)
    status=models.CharField(max_length=10)
    cm=models.CharField(max_length=4)
    dm_oracle=models.CharField(max_length=4)
    java_formater=models.CharField(max_length=4)
    java_Deai_js = models.CharField(max_length=4)
    pvt=models.CharField(max_length=20)
    testnap=models.CharField(max_length=20)
    bre=models.CharField(max_length=20)
    rre=models.CharField(max_length=20)
    syc_pdc=models.CharField(max_length=20)
    def __strt__(self):
        return self.servername
