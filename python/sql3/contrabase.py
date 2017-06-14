#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('/home/jroca72/eltao/web/db.sqlite3')

cursor = con.cursor()

print "la base de datos se abrió correctamente"

cursor.execute("SELECT id, temperatura, fecha  FROM bonito_temperatura")

for i in cursor:
    print "id : " , i[0], " Temperatura : ", i[1], "º", " Fecha: ", i[2]
print "Fin de la ejecución"

con.close
