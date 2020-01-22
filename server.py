# -*- coding:utf-8 -*-
from flask import Flask, Response, redirect, render_template
import os.path
import sqlite3 as lite
import time

app = Flask (__name__)
app.debug = True
database_filename = 'urlhit.db'
conn = lite.connect(database_filename)


def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/get/<type>')
def _get(type):
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    query = ("select count(*) from table1 where type='%s';" % type)
    cs.execute(query)
    cs.fetchall()
    for i in all_rows:
        print(i)
    cs.close()
    conn.close()

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
    conn = lite.connect(database_filename)
    cs = conn.cursor()
    query = "SELECT * FROM redirect;"
    cs.execute(query)
    all_rows = cs.fetchall()
    data = []
    for i in all_rows:
        data.append({i[1] : i[2]})
    for list in data:
        if type == 'facebook':
            if 'facebook' in list.keys():
                cs.execute("INSERT INTO hitlog (type, url, time) values ('facebook', 'https://www.facebook.com', DATETIME('NOW'))")
                conn.commit()
                cs.close()
                conn.close()
                return redirect(list['facebook'])
            else:
                continue
        elif type == 'naver':
            if 'naver' in list.keys():
                cs.execute("INSERT INTO hitlog (type, url, time) values ('naver', 'https://www.naver.com', DATETIME('NOW'))")
                conn.commit()
                cs.close()
                conn.close()
                return redirect(list['naver'])
            else:
                continue
        elif type == 'google':
            if 'google' in list.keys():
                cs.execute("INSERT INTO hitlog (type, url, time) values ('google', 'https://www.google.com', DATETIME('NOW'))")
                conn.commit()
                cs.close()
                conn.close()
                return redirect(list['google'])
            else:
                continue
        else:
            continue

if __name__ == "__main__":
    cs = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS hitlog (id INTEGER PRIMARY KEY AUTOINCREMENT, type VARCHAR(64), url VARCHAR(256), time DATETIME)"
    cs.execute(query)
    query = "CREATE TABLE IF NOT EXISTS redirect (id INTEGER PRIMARY KEY AUTOINCREMENT, type VARCHAR(64), redirecturl VARCHAR(256))"
    cs.execute(query)
    cs.execute("INSERT INTO redirect (type, redirecturl) values('facebook', 'https://www.facebook.com')")
    cs.execute("INSERT INTO redirect (type, redirecturl) values('naver', 'https://www.naver.com')")
    cs.execute("INSERT INTO redirect (type, redirecturl) values('google', 'https://www.google.com')")
    conn.commit()
    query = "DELETE from redirect WHERE id > 3;"
    cs.execute(query)
    conn.commit()
    cs.close()
    conn.close()
    app.run(host='0.0.0.0', port=5000)