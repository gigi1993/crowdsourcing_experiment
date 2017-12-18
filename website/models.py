from django.db import models
from django.utils import timezone


class Submission(models.Model):
    number = models.AutoField(primary_key=True)
    prolific_id = models.CharField(max_length=50, default='')
    spoofer_URL = models.CharField(max_length=70, default='')
    date = models.DateTimeField(default=timezone.now)
    ip_address = models.CharField(max_length=120, default='')
    asn = models.CharField(max_length=10, default='')

    def __str__(self):
        return "%s %s " %(self.prolific_id, self.spoofer_URL)

class Failed(models.Model):
    number = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    ip_address = models.CharField(max_length=120, default='')
    asn = models.CharField(max_length=10, default='')

    def __str__(self):
        return "%s %s " %(self.number, self.asn)

class Again(models.Model):
    number = models.AutoField(primary_key=True)
    prolific_id = models.CharField(max_length=50, default='')
    date = models.DateTimeField(default=timezone.now)
    ip_address = models.CharField(max_length=120, default='')
    asn = models.CharField(max_length=10, default='')

    def __str__(self):
        return "%s %s " %(self.prolific_id, self.spoofer_URL)

