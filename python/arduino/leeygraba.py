#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, datetime
import sqlite3
import serial

# lee arduino por serial/usb
# envía caracter 'e' y lee temperatura de sensor lm35

arduino=serial.Serial('/dev/ttyUSB0',baudrate=9600, timeout = 3.0)
cadena=''
grados = ''
arduino.write("e")
time.sleep(0.1)

while arduino.inWaiting() > 0:
            cadena += arduino.readline()
            #print cadena.rstrip('\n')
            #cadena = ''
arduino.close()
grados =  cadena.rstrip('\n')
# escribe la temperatura en la base sqlite3
conn = sqlite3.connect('/home/jroca72/eltao/web/db.sqlite3')
cursor = conn.cursor()

ahora = datetime.datetime.now()
registro = (grados, ahora)
cursor.execute("INSERT INTO bonito_temperatura  (temperatura, fecha) VALUES (?,?)", registro)
conn.commit()
# cerramos cursor y conexiones, mensaje de fin
cursor.close()
conn.close()
