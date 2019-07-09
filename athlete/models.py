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

class AssessmentEvent(models.Model):
    AssessmentDate = models.DateField(default = date.today)
    Location = models.TextField(default = 'Hithercroft')
    AvHeightJump = models.FloatField(default = 0)
    AvBroadJump = models.FloatField(default = 0)
    AvGripStrength = models.FloatField(default = 0)
    AvSprint = models.FloatField(default = 0)
    AvAgilityBox = models.FloatField(default = 0)
    AvFiveFromFiveTime = models.FloatField(default = 0)
    AvFiveFromFiveBalls = models.FloatField(default = 0)
    AvHitSpeed = models.FloatField(default = 0)
    AvPushSpeed = models.FloatField(default = 0)
    AvIRYY1 = models.FloatField(default = 0)
    Comments = models.TextField(default = 'None')

    def __str__(self):
        return '%s %s' % (self.Location, str(self.AssessmentDate))

    

class assessment(models.Model):
    
    HeightJump = models.FloatField(default = 0)
    BroadJump = models.FloatField(default = 0)
    GripStrength = models.FloatField(default = 0)
    Sprint = models.FloatField(default = 0)
    AgilityBox = models.FloatField(default = 0)
    FiveFromFiveTime = models.FloatField(default = 0)
    FiveFromFiveBalls = models.FloatField(default = 0)
    HitSpeed = models.FloatField(default = 0)
    PushSpeed = models.FloatField(default = 0)
    IRYY1 = models.FloatField(default = 0)
    IncludeInAverages = models.BooleanField(default = True)
    Comments = models.TextField()
    Athlete = models.ForeignKey(athlete, on_delete=models.CASCADE)
    AssessmentEvent_FK = models.ForeignKey(AssessmentEvent, on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.Athlete.AthleteName, str(self.AssessmentEvent_FK.AssessmentDate))
