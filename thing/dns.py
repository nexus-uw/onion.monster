import os
import requests


def updateIpv4(domain, ip):
  key = os.environ.get("GANDI_KEY")
  if key == None:
      raise Exception("GANDI_KEY not set")
  url = 'https://api.gandi.net/v5/livedns/domains/onion.monster/records'
  myobj = {
    "rrset_name":domain,
    "rrset_type":"A",
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
  # todo - be smart about this...
  if x.status_code >= 400:
     raise Exception("failed: "+x.text)
def updateIpv6(domain, ip):
   raise Exception("ass")

