#!/usr/bin/python
# -*- coding: utf-8 -*-

import virustotal

#v = virustotal.VirusTotal('d1835c92cd4dfdbdabd009309064f9a6a60d6337e3cd69978213ce52ce9fca7d')


'''import requests
params = {'apikey': 'd1835c92cd4dfdbdabd009309064f9a6a60d6337e3cd69978213ce52ce9fca7d', 'hash': 'e7b3f9065d168e45aaf2118afbe39617'}
response = requests.get('https://www.virustotal.com/vtapi/v2/file/download', params=params)
downloaded_file = response.content

print downloaded_file'''

#from __future__ import print_function
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

API_KEY = 'd1835c92cd4dfdbdabd009309064f9a6a60d6337e3cd69978213ce52ce9fca7d'

#EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
#EICAR_MD5 = hashlib.md5(EICAR).hexdigest()

vt = VirusTotalPublicApi(API_KEY)

response = vt.get_file_report('e7b3f9065d168e45aaf2118afbe39617')
print(json.dumps(response, sort_keys=False, indent=4))
