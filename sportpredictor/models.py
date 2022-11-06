import datetime
from email.policy import default
from pyexpat import model
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

    age = models.PositiveIntegerField(default=18)

    # dateofbirth=models.DateField(null=True, blank=True)

    nationality = models.CharField(max_length=50,default="Not Associated")
    Location = models.CharField(max_length=50,default="Not Associated")
    e_mail = models.EmailField(null=True, blank=True)
    tel=models.CharField(max_length=12,null=True, blank=True)


    # @property
    # def age(self):
    #     today = datetime.date.today()
    #     if self.dateofbirth:
    #         born = self.dateofbirth
    #     else:
    #         born = datetime.date(2000,4,3)
        
    #     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))




    @property
    def birth_year(self):
        now = datetime.date.today().year
        return (now-self.age)

    height= models.FloatField(null=True)
    weight = models.FloatField(null=True)
    armspan = models.FloatField(null=True)
    foot_length = models.FloatField(null=True)
    one_hand_length = models.FloatField(null=True)
    shoulder_size = models.FloatField(null=True)
    waist = models.FloatField(null=True)
    neck = models.FloatField(null=True)
    hip = models.FloatField(null=True)

    fat = models.FloatField(null=True)
    
    back_flexibility = models.FloatField(null=True)
    shoulder_flexibility = models.FloatField(null=True)
    finger_2 = models.FloatField(null=True)
    finger_4 = models.FloatField(null=True)
    super_test_1 = models.PositiveIntegerField(null=True)
    super_test_2 = models.PositiveIntegerField(null=True)
    super_test_3 = models.PositiveIntegerField(null=True)



    def __str__(self) -> str:
        return self.name


class sport(models.Model):
    en_name = models.CharField(max_length=50,default="None")
    fa_name = models.CharField(max_length=50,default="None")


    height_to_age= models.PositiveIntegerField(null=True)
    armspan = models.PositiveIntegerField(null=True)
    foot_length_to_age = models.PositiveIntegerField(null=True)
    one_hand_length_to_age = models.PositiveIntegerField(null=True)
    shoulder_size = models.PositiveIntegerField(null=True)
    fat = models.PositiveIntegerField(null=True)
    back_flexibility = models.PositiveIntegerField(null=True)
    shoulder_flexibility = models.PositiveIntegerField(null=True)
    finger_ratio = models.PositiveIntegerField(null=True)
    anaerobic =models.PositiveIntegerField(null=True)
    Lactic_anaerobic=models.PositiveIntegerField(null=True)
    Aerobic=models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.en_name


class medians(models.Model):
    name = models.CharField(max_length = 40,default="none")
    count = models.PositiveIntegerField(default=0)
    
    max = models.FloatField(default=0)
    min =models.FloatField(default=0)

    stage_1_min = models.FloatField(default=0)
    stage_1_max = models.FloatField(default=0)
    
    stage_2_min = models.FloatField(default=0)
    stage_2_max = models.FloatField(default=0)
    
    stage_3_min = models.FloatField(default=0)
    stage_3_max = models.FloatField(default=0)
    
    stage_4_min = models.FloatField(default=0)
    stage_4_max = models.FloatField(default=0)
    
    stage_5_min = models.FloatField(default=0)
    stage_5_max = models.FloatField(default=0)

    Average_value = models.FloatField(default=0)


    def __str__(self):
        return self.name
