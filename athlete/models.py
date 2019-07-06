from django.db import models

# Create your models here.
class athlete(models.Model):
    AthleteName = models.CharField(max_length=200)
    DoB = models.DateField('date of birth')

