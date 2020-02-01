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
    return render_template('index.html')

@app.route('/', methods=['POST'])
def _gettag():
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    
    cs.execute("SELECT COUNT(distinct redirecturl) FROM redirect;")
    urlCount = cs.fetchall()

    cs.execute("SELECT distinct redirecturl FROM redirect;")
    urls = cs.fetchall()
    resultList = {}
    stack = 1
    for i in urls:
        tmpList = {}
        tmpList["url"] = i[0]
        tags = {}
        cs.execute("SELECT tag FROM redirect WHERE redirecturl='%s'" % (i[0]))
        url = cs.fetchall()
        tagStack = 1
        for j in url:
            value = cs.execute("SELECT COUNT(*) From hitlog where k_redirect=(SELECT id FROM redirect WHERE redirecturl='%s' AND tag='%s');" % (i[0], j[0]))
            value = cs.fetchall()
            tags[j[0]] = value[0][0]
            tagStack = tagStack + 1
        tmpList["tags"] = tags
        cs.execute("SELECT shareurl FROM redirect WHERE redirecturl='%s'" % (i[0]))
        surl = cs.fetchall()
        surls = {}
        tagStack = 1
        for j in surl:
            surls[str(tagStack)] = j[0]
            tagStack = tagStack + 1
        tmpList["shortulrs"] = surls
        resultList[str(stack)] = tmpList
        stack = stack + 1
    data = {"Code": "200", "urlCount": urlCount[0][0], "urls": resultList}
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
        data = {"Code": "200", "url": 'http://www.urlhit.shop/'+compat_url, "size": 1, "tag": {"1":"Default"}}
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
    isOK = False
    redirecturl = request.get_json()['redirecturl']
    if 'https://' in redirecturl:
        isOK = True
    if 'http://' in redirecturl:
        isOK = True
    if isOK == False:
        redirecturl = 'https://' + redirecturl
    print(redirecturl)
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    cs.execute("SELECT COUNT(*) FROM redirect;")
    count = cs.fetchall()
    compat_url = URL_Shortener().shorten_url(redirecturl, count[0][0] + 1)
    cs.execute("INSERT INTO redirect (redirecturl, shareurl, tag) values ('%s', '%s', '%s')" % (redirecturl, compat_url, request.get_json()['tag']))
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
    data = {"Code": "201", "url": 'http://www.urlhit.shop/'+compat_url, "tag": request.get_json()['tag']}
    return data
'''
type = 유입 플랫폼
'''
@app.route('/url/<type>')
def redriect(type):
    if type == 'favicon.ico':
        pass
    else:
        conn = lite.connect(database_filename)
        cs = conn.cursor()
        query = "SELECT * FROM redirect WHERE shareurl='%s';" % (type)
        cs.execute(query)
        _data = cs.fetchall()
        cs.execute("INSERT INTO hitlog (k_redirect, url, time) values ('%s', '%s', DATETIME('NOW'))" % (_data[0][0], type))
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
    app.run(host='0.0.0.0', port=5000)