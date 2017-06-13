#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'arduino'


def run_query(query):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data



texto = "select temperatura, date_format(fecha, '%d/%m/%Y %H:%i:%s') from temperatura order by fecha desc"
registros = run_query(texto)

# comentario
for i in range(len(registros)):
    print registros[i][1] + ' -- ' + str(registros[i][0])
