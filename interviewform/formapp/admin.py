from django.contrib import admin
from formapp.models import interviewform
# Register your models here.

class formAdmin(admin.ModelAdmin):
    pass

admin.site.register(interviewform, formAdmin)
