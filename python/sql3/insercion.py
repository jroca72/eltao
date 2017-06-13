#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, datetime
import MySQLdb

#inicializacion
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'arduino'
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
conn = MySQLdb.connect(*datos)
cursor = conn.cursor()
t_end = time.time() + 60

#12 lecturas secuenciales
while time.time() < t_end:
    try:
        # inserción de datos en MySQL
        ahora = datetime.datetime.now()
        cursor.execute("INSERT INTO temperatura VALUES (%s,%s)",(13.5,ahora))
        conn.commit()
        time.sleep(5)
        print("registro grabado...")

    except:
        # error excepción -- vuelta atras
        conn.rollback()
        time.sleep(5)
        print("registro rechazado ...")

# cerramos cursor y conexiones, mensaje de fin
cursor.close()
conn.close()
print("fin de la grabacion...")
