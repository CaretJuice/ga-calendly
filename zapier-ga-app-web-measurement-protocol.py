import requests
from urllib.parse import urlencode, quote_plus
import re
import json
#config
tid = "" #App and Web TID starts G-xxxxxxxxxx
host = "https://www.google-analytics.com/g/collect"
cid = input_data['cid']

new_dict = {}
errors = []
out = {}

valid_cid = re.match( r"^[0-9]{9,10}\.[0-9]{10}$" , cid)
if valid_cid == None:
    errors.append('CID not valid for ' + tid  + ' ')

qs = { 
    'v' : 2,
    'tid' : tid, 
    'cid' : cid, 
    'en' : 'generate_lead',
    'ep.currency' : 'USD',
    'epn.value' : '50',
}

qs = urlencode(qs, quote_via=quote_plus)
transaction = host + "?" + qs
r = requests.post(transaction)

out['errors'] = errors
#returning errors to pass to another zap
return out