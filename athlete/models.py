from django.db import models

# Create your models here.
class athlete(models.Model):
    AthleteName = models.CharField(max_length=200)
    DoB = models.DateField('date of birth',null = True, blank=True)
    email = models.EmailField('email', null = True, blank=True)

    def __str__(self):
        return self.AthleteName