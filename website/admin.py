from django.contrib import admin
from .models import Submission
from .models import Failed
from .models import Again
from .models import AutonomousSystem

# Register your models here.
class AutonomousSystemAdmin(admin.ModelAdmin):
	list_display = ['number', 'timestamp', 'updated', 'asn', 'data_point']
	class Meta:
		model = Submission
admin.site.register(AutonomousSystem, AutonomousSystemAdmin)


class SubmissionAdmin(admin.ModelAdmin):
	list_display = ['number', 'date', 'country', 'asn', 'ip_address', 'ip_prefix', 'prolific_id', 'spoofer_URL']
	class Meta:
		model = Submission
admin.site.register(Submission, SubmissionAdmin)

class FailedAdmin(admin.ModelAdmin):
	list_display = ['number', 'date', 'country', 'asn', 'ip_address', 'ip_prefix', 'prolific_id']
	class Meta:
		model = Failed
admin.site.register(Failed, FailedAdmin)

class AgainAdmin(admin.ModelAdmin):
	list_display = ['number', 'date', 'country', 'asn', 'ip_address',  'ip_prefix', 'prolific_id']
	class Meta:
		model = Again
admin.site.register(Again, AgainAdmin)