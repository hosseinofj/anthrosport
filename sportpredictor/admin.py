from django.contrib import admin
from .models import target,sport,medians
import datetime
# Register your models here.

class targetAdmin(admin.ModelAdmin):

    list_display = ('pk','name','gender','age','shoulder_size','height','foot_length','armspan','back_flexibility','shoulder_flexibility')

class sportAdmin(admin.ModelAdmin):

    list_display = ('pk','en_name','fa_name','height_to_age',
                    'armspan',
                    'foot_length_to_age',
                    'one_hand_length_to_age',
                    'shoulder_size',
                    'fat',
                    'back_flexibility',
                    'shoulder_flexibility',
                    'finger_ratio',
                    'anaerobic',
                    'Lactic_anaerobic',
                    'Aerobic',
)

class mediansAdmin(admin.ModelAdmin):

    list_display = ('name','count','Average_value',"min","max")


admin.site.register(target,targetAdmin)
admin.site.register(sport,sportAdmin)
admin.site.register(medians,mediansAdmin)


