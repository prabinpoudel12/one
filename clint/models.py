from django.db import models

# Create your models here.
from django.db import models

class Clint_management(models.Model):
    name                        = models.CharField(max_length=200, null=True)
    companyname                     = models.CharField(max_length=200, null=True)
    contact                     = models.IntegerField()
    email                       = models.EmailField(max_length=200)
    pan                         = models.IntegerField(null=True)
    company_id                  = models.CharField(max_length= 200,)