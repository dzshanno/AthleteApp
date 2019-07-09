from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import athlete,assessment



class athleteAdmin(admin.ModelAdmin):
    list_display = ['AthleteName','email']
    list_filter = ['AthleteName']
    search_fields = ['AthleteName']

class assessmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(athlete, athleteAdmin)
admin.site.register(assessment, assessmentAdmin)