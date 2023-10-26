from django.db import models

# Create your models here.
class Users(models.Model):
    DocNum=models.CharField(max_length=11,null=False)
    Name=models.CharField(max_length=225,null=True)
    Password=models.CharField(max_length=225,null=True)

