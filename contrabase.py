#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

DB_HOST = '10.1.1.201'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'contabilidad'


def run_query(query):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data



texto = "select numero, date_format(fecha, '%d/%m/%Y'), nombre from facturas"
registros = run_query(texto)

for i in range(len(registros)):
    print str(registros[i][0]) + ' -- ' + registros[i][1] + ' -- ' + registros[i][2]
