# -*- coding:utf-8 -*-
import json
import os.path
import requests
import time

URL = 'https://script.google.com/macros/s/AKfycbzrmd2D4AnEa6LIZiUtOE64ybyyok_zaQYnXq8mfvcTR6CBFQ/exec?'
URL += "Type=" + 'facebook' + "&Url=" + 'https://www.naver.com' + "&Time=" + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
with requests.Session() as res:
    req = res.get(URL)
    if req.ok:
        print(req.ok)
