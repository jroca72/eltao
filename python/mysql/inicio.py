#!/usr/bin/env python
# -*- coding: utf-8 -*-


def letra_nif(dni):
    mi_lista=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E","O"]
    valor = dni / 23
    valor = valor * 23
    valor = dni - valor

    return mi_lista[valor]


dninumero = input("dame el número de dni : ")
letra = letra_nif(dninumero)
print "la letra del DNI es : " + letra
