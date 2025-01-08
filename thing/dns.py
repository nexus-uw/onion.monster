import os
import requests




from ipaddress import ip_address, IPv4Address

def isIpv4(IP: str) -> bool:
  return type(ip_address(IP)) is IPv4Address

# todo constants


def updateIp(domain, ip):
  key = os.environ.get("GANDI_KEY")
  if key == None:
      raise Exception("GANDI_KEY not set")
  url = 'https://api.gandi.net/v5/livedns/domains/onion.monster/records'
  myobj = {
    "rrset_name":domain,
    "rrset_type": "A" if(isIpv4(ip)) else "AAAA",
    "rrset_ttl":300, # best that gandi allows
    "rrset_values": [
      ip
    ]
  }
  headers = {
    "content-type": "application/json",
    "authorization":"Bearer "+key
    }

  x = requests.post(url, json = myobj, headers = headers)

# conflict (record already exists, update existing record)
  if x.status_code == 409:
    x = requests.put("https://api.gandi.net/v5/livedns/domains/onion.monster/records/"+domain+"/"+ "A" if(isIpv4(ip)) else "AAAA"
, json =  {
    "rrset_ttl":300, # best that gandi allows
    "rrset_values": [
      ip
    ]
  }, headers = headers)
  # todo - be smart about this...
  if x.status_code >= 400:
     raise Exception("failed: "+x.text)


