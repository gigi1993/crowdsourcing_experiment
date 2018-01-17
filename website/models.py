from django.db import models
from django.utils import timezone

# model for AS
class AutonomousSystem(models.Model):
    number = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)
    asn = models.CharField(max_length=15, default='')
    data_point = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" %(self.asn, self.data_point)

# model for complete submission
class Submission(models.Model):
    number = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=5, default='')
    asn = models.CharField(max_length=15, default='')
    ip_address = models.CharField(max_length=120, default='')
    ip_prefix = models.CharField(max_length=120, default='')
    prolific_id = models.CharField(max_length=50, default='')
    spoofer_URL = models.CharField(max_length=70, default='')

    def __str__(self):
        return "%s %s %s %s %s %s" %(self.country, self.asn, self.ip_address, self.ip_prefix, self.prolific_id, self.spoofer_URL)

# model for failed submission
class Failed(models.Model):
    number = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    prolific_id = models.CharField(max_length=50, default='')
    ip_address = models.CharField(max_length=120, default='')
    ip_prefix = models.CharField(max_length=120, default='')
    asn = models.CharField(max_length=15, default='')
    country = models.CharField(max_length=5, default='')

    def __str__(self):
        return "%s %s %s %s %s" %(self.country, self.asn, self.ip_address, self.ip_prefix, self.prolific_id)

# model for retest
class Again(models.Model):
    number = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    prolific_id = models.CharField(max_length=50, default='')
    ip_address = models.CharField(max_length=120, default='')
    ip_prefix = models.CharField(max_length=120, default='')
    asn = models.CharField(max_length=15, default='')
    country = models.CharField(max_length=5, default='')

    def __str__(self):
        return "%s %s %s %s %s" %(self.country, self.asn, self.ip_address, self.ip_prefix, self.prolific_id)