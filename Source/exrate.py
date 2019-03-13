# -*- coding: utf-8 -*-
# @Author: null

import re
import json
import urllib.request

url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXJPYCNY&column=Code,Price"
req = urllib.request.Request(url)
f = urllib.request.urlopen(req)
html = f.read().decode("utf-8")
print(html)

s = re.findall("{.*}",str(html))[0]
sjson = json.loads(s)

JPYCNY = sjson["Data"][0][0][1]/10000
print(JPYCNY)
