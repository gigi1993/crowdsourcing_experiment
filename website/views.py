from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SubmissionForm
from .forms import AgainForm
from .forms import FailedForm
from website.models import Submission
from website.models import Failed
from website.models import Again
from website.models import AutonomousSystem
from django.core.exceptions import ObjectDoesNotExist
#import pyasn
#import math
#from geolite2 import geolite2

# Function that get user's IP
def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

# Function that lookup the AS given the IP
# def get_asn(ip):
#     asndb = pyasn.pyasn('/home/infospoofing/crowdsourcing_experiment/ipasn.dat')        # Initialize database ASN
#     asn = asndb.lookup(ip)[0]
#     return asn

# Function that retun number of datapoint given AS
# def get_dataPoint(asn):
#     db = pyasn.pyasn('/home/infospoofing/crowdsourcing_experiment/ipasn.dat')        # Initialize database ASN
#     all_prefixes = db.get_as_prefixes_effective(asn)
#     size = 0
#     if all_prefixes:
#         for prefix in all_prefixes:
#             pref = prefix.split("/")[1]
#             size = size + (2**(32-int(pref)))
#     dt_points = math.ceil(size/2097152)
#     return dt_points

# Function that return the country code given the IP
# def get_country_code(ip):
#     reader = geolite2.reader()              # get the Country code using GeoLite2
#     result = reader.get(ip)                 # create a dictionary with different fields ({city}, {country}...)
#     geolite2.close()
#     code=result['country']['iso_code']      #lookup
#     return code

# Function that return the right completion code given user's IP
# def get_completion_code(ip):
#     code = get_country_code(ip)
#     # depending on the iso_code, give right completion_code
#     if code == "NL":
#         completion_code = "https://www.prolific.ac/submissions/complete?cc=NL"
#     elif code == "FR":
#         completion_code = "https://www.prolific.ac/submissions/complete?cc=XXXXXXXX"
#     else:
#         completion_code = "DEFAULT"
#     return completion_code

# def get_prefix(ip):
#     secondByte = int([ byte for byte in ip.split('.') ][1])
#     secondByte_bin = (bin(secondByte)[2:])
#     prefixbyte_bin = ''
#     prefixbyte_dec = 0
#     if len(secondByte_bin) == 8:
#         prefixbyte_bin = secondByte_bin[:3]+'00000'
#         prefixbyte_dec = int(prefixbyte_bin ,2)
#     elif len(secondByte_bin) == 7:
#         prefixbyte_bin = secondByte_bin[:2]+'00000'
#         prefixbyte_dec = int(prefixbyte_bin ,2)
#     elif len(secondByte_bin) == 6:
#         prefixbyte_bin = secondByte_bin[:1]+'00000'
#         prefixbyte_dec = int(prefixbyte_bin ,2)
#     prefix = ip.split('.')[0]+"."+str(prefixbyte_dec)+".0.0/11"

#     return prefix

def homepage(request):
    current_IP = "123123"
    current_country = "XXX"
    current_ASN = "123"
    completion_code = "DEFAULT"
    prefix = "00000"
    # current_IP = get_ip(request)                            # Get user's IP
    # current_country = get_country_code(current_IP)          # Get user's country
    # country_not_ok = True                                   # initialise country_ok

# ###### new filtering
#     #(1) on country
#     if current_country == "NL":                     # check if user is in a selected country
#         country_not_ok = False
#     elif current_country == "FR":
#         country_not_ok = False
#     if country_not_ok:                              # if country is not ok, redirect to /fail
#         return redirect('fail')
#     #(2) on prefix
#     current_ASN = get_asn(current_IP)               # Get user's ASN
#     dt_point = get_dataPoint(current_ASN)
#     if not AutonomousSystem.objects.filter(asn=current_ASN).exists():       # if ASN is not in listAS
#         a = AutonomousSystem.objects.create(asn=current_ASN, data_point=dt_point) # add ASN and datapoint

#     prefix = get_prefix(current_IP)                     # get /11
#     if Submission.objects.filter(ip_prefix=prefix).exists(): # if /11 already tested
#         return redirect('fail')                         # fail

#     # if Submission.ASN.count >= dataPoint
#     if Submission.objects.filter(ip_prefix=prefix).count() >= dt_point:
#         return redirect('fail')

###### Else go on and show instructions

    if request.method == "POST":                            # Submission form
        form = SubmissionForm(request.POST)                 # Create new SUBMISSION
        if form.is_valid():                                 # Assign all fields...
            submission = form.save(commit=False)
            submission.date = timezone.now()
            submission.ip_address = current_IP
            submission.asn = current_ASN
            submission.country=current_country
            submission.ip_prefix = prefix
            submission.save()
            return redirect('success')                      # Redirect to /success
    else:
        form = SubmissionForm()                             # Else (form not valid) reload the page
    return render(request, 'website/homepage.html', {'form': form})

def success(request):                                       # After correct submission
    # current_IP = get_ip(request)                            # Get user's IP
    # completion_code = get_completion_code(current_IP)       # based on IP, get completion code
    current_IP = "123123"
    current_country = "XXX"
    current_ASN = "123"
    completion_code = "DEFAULT"
    prefix = "00000"
    if request.method == "POST":
        form = AgainForm(request.POST)                      # If user wants to do the test again in the future
        if form.is_valid():                                 # Assign all fields...
            again = form.save(commit=False)
            again.date = timezone.now()
            # again.ip_address = get_ip(request)
            # again.asn = get_asn(current_IP)
            # again.ip_prefix = get_prefix(current_IP)
            # again.country=get_country_code(current_IP)
            again.ip_address = current_IP
            again.asn = current_ASN
            again.ip_prefix = prefix
            again.country=current_country
            again.save()
            return redirect('end')                          # Redirect to /end
    else:                                                   # Else (form non valid), reload page
        form = AgainForm()
    return render(request, 'website/success.html', {'form': form, 'completion_code': completion_code})

def fail(request):
    current_country = "XXX"
    current_ASN = "123"
    completion_code = "DEFAULT"
    prefix = "00000"                                          # When the ASN is already tested
    #current_IP = get_ip(request)                            # get user's IP
    if request.method == "POST":
        form = FailedForm(request.POST)                     # Create FAILED
        if form.is_valid():                                 # Assign all fields...
            failed = form.save(commit=False)
            failed.date = timezone.now()
            # failed.ip_address = get_ip(request)
            # failed.asn = get_asn(current_IP)
            # failed.country=get_country_code(current_IP)
            # failed.ip_prefix = get_prefix(current_IP)
            failed.ip_address = current_IP
            failed.asn = current_ASN
            failed.country=current_country
            failed.ip_prefix = prefix
            failed.save()
            return redirect('finish')                       # Redirect to /end
    else:                                                   # Else (form non valid), reload page
        form = FailedForm()
    return render(request, 'website/fail.html', {'form': form})

def finish(request):                                        # Successful onclusion
    return render(request, 'website/finish.html', {})
def end(request):                                           # Fail conclusion
    return render(request, 'website/end.html', {})