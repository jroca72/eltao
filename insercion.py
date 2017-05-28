#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, datetime
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'arduino'

ahora = datetime.datetime.now()
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
conn = MySQLdb.connect(*datos)
cursor = conn.cursor()
try:
   cursor.execute("INSERT INTO temperatura VALUES (%s,%s)",(13.5,ahora))
   conn.commit()
except:
   conn.rollback()

cursor.close()
conn.close()
print("registro grabado...")
