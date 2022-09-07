import datetime
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

    height= models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    armspan = models.IntegerField(null=True)
    foot_length = models.IntegerField(null=True)
    one_hand_length = models.IntegerField(null=True)
    shoulder_size = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name