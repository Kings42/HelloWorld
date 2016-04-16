# -*- coding: utf-8 -*-
lista1 = []
lista2 = []
continuar = int(raw_input("¿Cuantas personas desea añadir?: "))

while int (continuar) != len (lista1):
    personas=str(raw_input("Nombre de la persona: "))
    lista1.append(personas)
    edades=str(raw_input("Edad de la persona: "))
    lista2.append(edades)
    print ""
    print "Ha ingresado", len (lista1), "personas"
    print "--------------------------------"

p=len(lista1)
mayor=0
for i in range (p):
    if lista1[i] > mayor:
        mayor = lista1[i]
print "El numero mayor es", mayor

    
