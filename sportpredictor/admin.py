from django.contrib import admin
from .models import target
import datetime
# Register your models here.

class targetAdmin(admin.ModelAdmin):

    # ...
    list_display = ('pk','name','gender','age','nationality','height','weight','armspan')


admin.site.register(target,targetAdmin)