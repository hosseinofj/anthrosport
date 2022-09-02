import email
from pyexpat import model
from django.db import models

# Create your models here.

def target_name_creator(instance):
    nums = target.objects.count()
    return "target_"+str(nums)
            



class target(models.Model):
    name = models.CharField(max_length=50,default=target_name_creator)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    dateofbirth=models.DateField(null=True, blank=True)

    nationality = models.CharField(max_length=50,default="Not Associated")
    Location = models.CharField(max_length=50,default="Not Associated")
    e_mail = models.EmailField()
    tel=models.CharField(max_length=12,null=True, blank=True)


    height= models.IntegerField()
    weight = models.IntegerField()
    armspan = models.IntegerField()
    foot_length = models.IntegerField()
    one_hand_length = models.IntegerField()
    shoulder_size = models.IntegerField()