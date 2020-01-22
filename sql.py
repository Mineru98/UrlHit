# -*- coding:utf-8 -*-
import sqlite3 as lite
import time

database_filename = 'urlhit.db'
conn = lite.connect(database_filename)
cs = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS table1 (id INTEGER PRIMARY KEY AUTOINCREMENT, type VARCHAR(64), url VARCHAR(256), count INTEGER DEFAULT 1, time DATETIME)"
cs.execute(query)

#insert table
cs.execute("INSERT INTO table1 (type, url, time) values ('facebook', 'https://www.facebook.com', DATETIME('NOW'))")
conn.commit()

cs.close()
conn.close()