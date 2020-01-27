# -*- coding:utf-8 -*-
from flask import Flask, redirect, render_template, request
import sqlite3 as lite
from short import *

app = Flask (__name__)
app.debug = True
database_filename = 'urlhit.db'
conn = lite.connect(database_filename)

'''
마케팅 요소 첨가(SEO) 
'''
@app.route('/')
def _init():
    user = 'UrlHit'
    return render_template('index.html', name=user)

@app.route('/', methods=['POST'])
def _gettag():
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    cs.execute("SELECT tag from redirect;")
    tags = cs.fetchall()
    cs.execute("SELECT redirecturl from redirect;")
    urls = cs.fetchall()
    data = {"Code": "200", "size": len(tags), "urls": None, "tags": None, "hitcount": None}
    list = {}
    vList = {}
    uList = {}
    stack = 1
    for i in urls:
        uList[stack] = i[0]
        stack = stack + 1
    stack = 1
    for i in tags:
        query = "SELECT COUNT(*) from hitlog WHERE k_redirect in (SELECT id from redirect WHERE redirecturl='%s' AND tag='%s');" % (urls[stack-1][0], i[0])
        cs.execute(query)
        count = cs.fetchall()
        vList[stack] = count[0][0]
        list[stack] = i[0]
        stack = stack + 1
    data["tags"] = list
    data["hitcount"] = vList
    data["urls"] = uList
    cs.close()
    conn.close()
    return data

@app.route('/apply')
def _apply():
    return render_template('apply.html')

@app.route('/search', methods=['POST'])
def _search():
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    query = "SELECT COUNT(*) FROM redirect WHERE redirecturl='%s' and tag='Default';" % (request.get_json()['url'])
    cs.execute(query)
    count = cs.fetchall()
    if count[0][0] == 0:
        cs.execute("SELECT COUNT(*) FROM redirect;")
        _count = cs.fetchall()
        compat_url = URL_Shortener().shorten_url(request.get_json()['url'], _count[0][0] + 1)
        cs.close()
        conn.close()
        data = {"Code": "200", "url": 'https://urlhit.run.goorm.io/'+compat_url, "size": 1, "tag": {"1":"Default"}}
        return data
    elif count[0][0] > 0:
        cs.execute("SELECT tag FROM redirect WHERE redirecturl='%s';" % (request.get_json()['url']))
        _tag = cs.fetchall()
        cs.close()
        conn.close()
        data = {"Code": "409", "size": len(_tag), "tag": None}
        list = {}
        stack = 1
        for i in _tag:
            list[stack] = i[0]
            stack = stack + 1
        data["tag"] = list
        return data

@app.route('/apply', methods=['POST'])
def _applyurl():
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    cs.execute("SELECT COUNT(*) FROM redirect;")
    count = cs.fetchall()
    compat_url = URL_Shortener().shorten_url(request.get_json()['redirecturl'], count[0][0] + 1)
    cs.execute("INSERT INTO redirect (redirecturl, shareurl, tag) values ('%s', '%s', '%s')" % (request.get_json()['redirecturl'], compat_url, request.get_json()['tag']))
    conn.commit()
    cs.close()
    conn.close()
    data = {"Code": "201"}
    return data

@app.route('/tag/add', methods=['POST'])
def _addtag():
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    cs.execute("SELECT COUNT(*) FROM redirect;")
    count = cs.fetchall()
    compat_url = URL_Shortener().shorten_url(request.get_json()['redirecturl'], count[0][0] + 1)
    cs.close()
    conn.close()
    data = {"Code": "201", "url": 'https://urlhit.run.goorm.io/'+compat_url, "tag": request.get_json()['tag']}
    return data
'''
type = 유입 플랫폼
'''
@app.route('/<type>')
def redriect(type):
    if type == 'favicon.ico':
        pass
    else:
        conn = lite.connect(database_filename)
        cs = conn.cursor()
        query = "SELECT * FROM redirect WHERE shareurl='%s';" % (type)
        cs.execute(query)
        _data = cs.fetchall()
        cs.execute("INSERT INTO hitlog (k_redirect, url, time) values ('%s', '%s', DATETIME('NOW'))" % (type, _data[0][2]))
        conn.commit()
        cs.close()
        conn.close()
        return redirect(_data[0][1])

@app.route('/get/<type>')
def _get(type):
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    query = ("SELECT COUNT(*) FROM hitlog WHERE url='%s';" % (type))
    cs.execute(query)
    _count = cs.fetchone()
    cs.close()
    conn.close()
    return render_template('get.html', name=type, count=_count[0])

if __name__ == "__main__":
    cs = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS redirect (id INTEGER PRIMARY KEY AUTOINCREMENT, redirecturl VARCHAR(256), shareurl VARCHAR(256), tag VARCHAR(64) DEFAULT 'Default')"
    cs.execute(query)
    query = "CREATE TABLE IF NOT EXISTS hitlog (id INTEGER PRIMARY KEY AUTOINCREMENT, k_redirect INTEGER, url VARCHAR(256), time DATETIME, FOREIGN KEY(k_redirect) REFERENCES redirect(id))"
    cs.execute(query)
    app.run(host='0.0.0.0', port=80)