from django.db import models



# Create your models here.

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    age=models.IntegerField()
    # email = models.EmailField()
    # male = models.BooleanField(default=True)
    # female = models.BooleanField(default=False)
    # b_date = models.DateField(auto_now_add=True)
    # play = models.TimeField(auto_now=True)



class MyUser(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
