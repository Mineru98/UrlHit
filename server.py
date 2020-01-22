# -*- coding:utf-8 -*-
from flask import Flask, Response, redirect
import json
import os.path
import requests
import time

app = Flask (__name__)
app.debug = True

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

with open(str(os.path.join(root_dir(), 'data.json')),'rb') as f:
  data = json.load(f)

'''
마케팅 요소 첨가(SEO) 
'''
@app.route('/')
def _init():
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

'''
type = 유입 플랫폼
'''
@app.route('/<type>')
def redriect(type):
    URL = 'https://script.google.com/macros/s/AKfycbzrmd2D4AnEa6LIZiUtOE64ybyyok_zaQYnXq8mfvcTR6CBFQ/exec?'
    for list in data:
        if type == 'facebook':
            if 'facebook' in list.keys():
                URL += "Type=" + str(type) + "&Url=" + str(list['facebook']) + "&Time=" + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
                print(URL)
                with requests.Session() as res:
                    req = res.get(URL)
                    if req.ok:
                        print(req.ok)
                        return redirect(list['facebook'])
            else:
                continue
        elif type == 'naver':
            if 'naver' in list.keys():
                URL += "Type=" + str(type) + "&Url=" + str(list['naver']) + "&Time=" + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
                print(URL)
                with requests.Session() as res:
                    req = res.get(URL)
                    if req.ok:
                        print(req.ok)
                        return redirect(list['naver'])
            else:
                continue
        elif type == 'google':
            if 'google' in list.keys():
                URL += "Type=" + str(type) + "&Url=" + str(list['google']) + "&Time=" + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
                print(URL)
                with requests.Session() as res:
                    req = res.get(URL)
                    if req.ok:
                        print(req.ok)
                        return redirect(list['google'])
            else:
                continue
        else:
            continue

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)