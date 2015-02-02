#!/usr/bin/python

fich=open("/etc/passwd","r")
lista=fich.readlines()
diccionario = {}
claves = ["root", "imaginario"]

for linea in lista:
    conf = linea.split(":")
    usu = conf[0]
    shell = conf[-1]
    diccionario[usu] = shell    

for clave in claves:
    if diccionario.has_key(clave)==1:
        print "para el usuario",clave,":",diccionario         [clave]
    else:
        print "para la clave",clave,": no existe"
