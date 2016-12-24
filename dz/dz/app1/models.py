from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class Department(models.Model):
    name=models.CharField(max_length=40);
    leader=models.CharField(max_length=40);
    main_speciality=models.CharField(max_length=40);
    number_of_members=models.IntegerField(max_length=4);
    #worker=models.ForeignKey(Worker)

class Worker(models.Model):
    name=models.CharField(max_length=40);
    gift=models.IntegerField(max_length=5);
    department=models.ManyToManyField(Department, related_name='workers',blank=True,null=True);
    #user=models.OneToOneField(User)


