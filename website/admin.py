from django.contrib import admin
from .models import Submission
from .models import Failed
from .models import Again

# Register your models here.
class SubmissionAdmin(admin.ModelAdmin):  
	list_display = ['number', 'prolific_id', 'spoofer_URL', 'date', 'asn', 'ip_address']
	class Meta:
		model = Submission

admin.site.register(Submission, SubmissionAdmin)

class FailedAdmin(admin.ModelAdmin):  
	list_display = ['number', 'date', 'asn', 'ip_address']
	class Meta:
		model = Failed

admin.site.register(Failed, FailedAdmin)

class AgainAdmin(admin.ModelAdmin):  
	list_display = ['number', 'prolific_id', 'date', 'asn', 'ip_address']
	class Meta:
		model = Again

admin.site.register(Again, AgainAdmin)