from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from thing.dns import updateIp
from thing.models import Record

# Create your views here.

def index(request):
    context = {}
    return render(request, "thing/index.html", context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




def update(request:HttpRequest):
    domains = request.GET.get("domains") # todo ensure only 1 domain
    token = request.GET.get("token")
    # todo - validate token against DB + domain(s)
  #  ipv4=request.GET.get("ip")
  #  ipv6=request.GET.get("ipv6")
    client_addr = get_client_ip(request)

    record = get_object_or_404(Record, pk=token)

    if record.domain != domains:
       raise Exception("domain does not match domain from db for given key, should be 4xx error")

   # if(ipv4 == None && ipv6 == None)

    clear = request.GET.get("clear","false")
# domains={YOURVALUE}&token={YOURVALUE}[&ip={YOURVALUE}][&ipv6={YOURVALUE}][&verbose=true][&clear=true]
    updateIp(domains.replace(".onion.monster",""), client_addr)

    return render(request, "polls/detail.html", {})

