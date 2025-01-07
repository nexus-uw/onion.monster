from django.http import HttpRequest
from django.shortcuts import render

from thing.dns import updateIpv4, updateIpv6

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





from ipaddress import ip_address, IPv4Address

def isIpv4(IP: str) -> bool:
  type(ip_address(IP)) is IPv4Address

def update(request:HttpRequest):
    domains = request.GET.get("domains")
    token = request.GET.get("token")
    # todo - validate token against DB + domain(s)
  #  ipv4=request.GET.get("ip")
  #  ipv6=request.GET.get("ipv6")
    client_addr = get_client_ip(request)

   # if(ipv4 == None && ipv6 == None)

    clear = request.GET.get("clear","false")
# domains={YOURVALUE}&token={YOURVALUE}[&ip={YOURVALUE}][&ipv6={YOURVALUE}][&verbose=true][&clear=true]
    if (isIpv4(client_addr)):
      updateIpv4(domains.replace(".onion.monster",""), client_addr)
    else:
      updateIpv6(domains.replace(".onion.monster",""), client_addr)

    return render(request, "polls/detail.html", {})

