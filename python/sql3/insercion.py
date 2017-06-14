#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, datetime
import sqlite3

conn = sqlite3.connect('/home/jroca72/eltao/web/db.sqlite3')
cursor = conn.cursor()

ahora = datetime.datetime.now()
registro = (25.5, ahora)
cursor.execute("INSERT INTO bonito_temperatura  (temperatura, fecha) VALUES (?,?)", registro)
conn.commit()
# cerramos cursor y conexiones, mensaje de fin
cursor.close()
conn.close()
print("fin de la grabacion...")
