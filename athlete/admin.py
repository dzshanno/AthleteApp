from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import athlete



class athleteAdmin(admin.ModelAdmin):
    list_display = ['AthleteName','email']
    list_filter = ['AthleteName']
    search_fields = ['AthleteName']

admin.site.register(athlete, athleteAdmin)