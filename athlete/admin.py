from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import athlete

admin.site.register(athlete)

class athleteAdmin(admin.ModelAdmin):
    list_display = ['AthleteName','email']