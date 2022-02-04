from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=225)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.TextField(null=True, blank=True)
    meetingagenda=models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.meetingtitle

    class Meta:
        db_table="Meeting"

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.meetingID

    class Meta:
        db_table="MeetingMinutes"

class Resource(models.Model):
    resourcename=models.CharField(max_length=225)
    resourcetype=models.CharField(max_length=225)
    resourceURL=models.URLField()
    enterdate=models.DateField()
    userID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescrip=models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.resourcename

    class Meta:
        db_table="Resource"

class Event(models.Model):
    eventtitle=models.CharField(max_length=225)
    eventlocation=models.CharField(max_length=225)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescrip=models.TextField(null=True, blank=True)
    userIDmember=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table="Event"