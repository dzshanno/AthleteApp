from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class athlete(models.Model):
    AthleteName = models.CharField(max_length=200)
    DoB = models.DateField('date of birth',null = True, blank=True)
    email = models.EmailField('email', null = True, blank=True)
    guardian = models.ManyToManyField(User)

    def __str__(self):
        return self.AthleteName


class assessment(models.Model):
    AssessmentDate = models.DateField(default = date.today)
    HeightJump = models.FloatField()
    BroadJump = models.FloatField()
    GripStrength = models.FloatField()
    Sprint = models.FloatField()
    AgilityBox = models.FloatField()
    FiveFromFiveTime = models.FloatField()
    FiveFromFiveBalls = models.FloatField()
    HitSpeed = models.FloatField()
    PushSpeed = models.FloatField()
    IYRR1 = models.FloatField()
    Comments = models.TextField()
    Athlete = models.ForeignKey(athlete, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.Athlete, str(self.AssessmentDate))