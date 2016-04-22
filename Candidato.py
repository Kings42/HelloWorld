# -*- coding: utf-8 -*-
var = int (raw_input("Cuantos dias desea registrar?: "))
lista1 = []
lista2 = []
n=0
p=0
parar=True
l=0
dato=0
info=0
dia=int
bajando=False

while len(lista1)!=var:
    n=n+1
    print "---------------------------------------------------------"
    print "Dia", n
    while parar == True:
        print ""
        var1 = int (raw_input("Ingrese el nivel de popularidad de entre 2% y 100%: "))
        if var1 > 1 and var1 < 101:
            parar = False
    lista1.append(var1)
    l=l+1
    lista2.append(l)
    p=var-len(lista1)
    print "Le faltan ingresar", p, "dias."
    print ""
    p=0
    var1=0
    parar=True


mayor=0
for i in range (len(lista1)):
    if lista1[i] > mayor:
        mayor = lista1[i]
while mayor != dia:
    dato=dato+1
    dia=lista1[info]
    info=info+1

grande=mayor
minimo=(mayor*15)/100
rango=var-dato

for r in range (lista1[rango]):
    if r < minimo:
        bajando=True  

print "---------------------------------------------------------"
print "En el dia", dato, "consiguio la mayor popularidad con", mayor, "porciento."
if bajando == True:
    print "---------------------------------------------------------"
    print "Su popularidad desde el dia", dato, "en el cual obtuvo el mayor porcentaje, ha descendido de forma subita"

    



