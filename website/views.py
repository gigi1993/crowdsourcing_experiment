from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SubmissionForm
from .forms import AgainForm
#import pyasn
from website.models import Submission
from website.models import Failed
from website.models import Again
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def get_ip(request):                        # Function that get user'split IP
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

#def get_asn(ip):                            # Function that lookup the AS given the IP
#    asndb = pyasn.pyasn('ipasn.dat')        # Initialize database ASN
#    asn = asndb.lookup(ip)[0]               # Lookup IP
#    return asn
    
def homepage(request):
#    current_IP = '193.173.216.238'           # test
    current_IP = get_ip(request)            # Get user's IP
#    current_ASN = get_asn(current_IP)       # Get user's ASN
    if Submission.objects.filter(ip_address=current_IP): # (asn=current_ASN).exists(): # If the ASN is already in our database...
        return redirect('fail')             # NO TEST, goto /fail
                                            # Else go on and show instructions
    if request.method == "POST":            # Submission form
        form = SubmissionForm(request.POST) # Create new SUBMISSION
        if form.is_valid():                 # Assign all fields...
            submission = form.save(commit=False)
            submission.date = timezone.now()
            submission.ip_address = get_ip(request)            
#            submission.asn = get_asn(current_IP)
            submission.save()
            return redirect('success')      # Redirect to /success
    else:
        form = SubmissionForm()             # Else (form not valid) reload the page
    return render(request, 'website/homepage.html', {'form': form})
#def contacts(request):
#    return render(request, 'website/contacts.html', {})

def success(request):                           # After correct submission
#    current_IP = '193.173.216.238'
    current_IP = get_ip(request)               # Get user's IP
    if request.method == "POST":
        form = AgainForm(request.POST)          # If user want to do the test again in the future
        if form.is_valid():                     # Assign all fields...
            again = form.save(commit=False)
            again.date = timezone.now()
            again.ip_address = get_ip(request)            
#            again.asn = get_asn(current_IP)
            again.save()
            return redirect('end')              # Redirect to /end
    else:                                       # Else (form non valid), reload page
        form = AgainForm()
    return render(request, 'website/success.html', {'form': form})

def fail(request):                              # When the ASN is already tested
    current_IP = get_ip(request)                # get user's IP
#    current_IP = '193.173.216.238'           # test
#    current_ASN = get_asn(current_IP)      # lookup ASN
    Failed.objects.create(ip_address=current_IP)#, asn=current_ASN)   # Save failed attempt
    return render(request, 'website/fail.html', {})

def end(request):                               # Conclusion
    return render(request, 'website/end.html', {})