from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class athlete(models.Model):
    AthleteName = models.CharField(max_length=200)
    DoB = models.DateField('date of birth',null = True, blank=True)
    email = models.EmailField('email', null = True, blank=True)
    guardian = models.ManyToManyField(User)

    def __str__(self):
        return self.AthleteName