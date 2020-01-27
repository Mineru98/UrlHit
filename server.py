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

@app.route('/apply')
def _apply():
    return render_template('apply.html')

@app.route('/search', methods=['POST'])
def _search():
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    query = "SELECT COUNT(*) FROM redirect WHERE redirecturl='%s';" % (request.get_json()['url'])
    cs.execute(query)
    count = cs.fetchall()
    if count[0][0] == 0:
        cs.execute("SELECT COUNT(*) FROM redirect;")
        _count = cs.fetchall()
        compat_url = URL_Shortener().shorten_url(request.get_json()['url'], _count[0][0] + 1)
        data = {"Code": "200", "url": compat_url}
        return data
    elif count[0][0] > 0:
        data = {"Code": "409"}
        return data

@app.route('/apply', methods=['POST'])
def _applyurl():
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    cs.execute("SELECT COUNT(*) FROM redirect;")
    count = cs.fetchall()
    compat_url = URL_Shortener().shorten_url(request.get_json()['redirecturl'], count[0][0] + 1)
    cs.execute("INSERT INTO redirect (redirecturl, shareurl) values ('%s', '%s')" % (request.get_json()['redirecturl'], compat_url[28:]))
    # cs.execute("INSERT INTO redirect (redirecturl, shareurl) values ('%s', '%s')" % (request.get_json()['redirecturl'], compat_url[23:]))
    conn.commit()
    cs.close()
    conn.close()
    data = {"Code": "201"}
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
    query = "CREATE TABLE IF NOT EXISTS hitlog (id INTEGER PRIMARY KEY AUTOINCREMENT, k_redirect INTEGER, tag VARCHAR(64) DEFAULT 'default', url VARCHAR(256), time DATETIME, FOREIGN KEY(k_redirect) REFERENCES redirect(id))"
    cs.execute(query)
    query = "CREATE TABLE IF NOT EXISTS redirect (id INTEGER PRIMARY KEY AUTOINCREMENT, redirecturl VARCHAR(256), shareurl VARCHAR(256))"
    cs.execute(query)
    app.run(host='0.0.0.0', port=80)