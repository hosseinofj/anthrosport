import datetime
from unicodedata import name
from django.db import models

# Create your models here.

def target_name_creator():
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


    @property
    def age(self):
        today = datetime.date.today()
        if self.dateofbirth:
            born = self.dateofbirth
        else:
            born = datetime.date(2000,4,3)
        
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    height= models.PositiveIntegerField(null=True)
    weight = models.PositiveIntegerField(null=True)
    armspan = models.PositiveIntegerField(null=True)
    foot_length = models.PositiveIntegerField(null=True)
    one_hand_length = models.PositiveIntegerField(null=True)
    shoulder_size = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.name


class sport(models.Model):
    en_name = models.CharField(max_length=50,default="None")
    fa_name = models.CharField(max_length=50,default="None")


    height= models.PositiveIntegerField(null=True)
    armspan = models.PositiveIntegerField(null=True)
    foot_length = models.PositiveIntegerField(null=True)
    one_hand_length = models.PositiveIntegerField(null=True)
    shoulder_size = models.PositiveIntegerField(null=True)
