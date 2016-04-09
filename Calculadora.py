# -*- coding: utf-8 -*-
print"Calculadora"
var = (raw_input("¿Que operacion desea hacer? (suma, resta, multiplicacion, division, residuo) "))
if var == "suma":
    var3 = int (raw_input("Ingrese un numero: "))
    var4 = int (raw_input("Ingrese un numero: ")) 
    print "Suma:", var3 + var4
    if var3%var4%2==0:
        print"Numero par"
    if var3%var4%2!=0:
        print"Numero impar"
if var == "resta":
    var5 = int (raw_input("Ingrese un numero: "))
    var6 = int (raw_input("Ingrese un numero: ")) 
    print "Resta:", var5 - var6
    if var5%var6%2==0:
        print"Numero par"
    if var5%var6%2!=0:
        print"Numero impar"
if var == "multiplicacion":
    var7 = int (raw_input("Ingrese un numero: "))
    var8 = int (raw_input("Ingrese un numero: ")) 
    print "Multiplicacion:", var7 * var8
    if var7%var8%2==0:
        print"Numero par"
    if var7%var8%2!=0:
        print"Numero impar"
if var == "division":
    var9 = int (raw_input("Ingrese un numero: "))
    var10 = int (raw_input("Ingrese un numero: ")) 
    print "Division:", var9 / var10
    if var != 0:
        print var9/var10
    if var9%var10%2==0:
        print"Numero par"
    if var9%var10%2!=0:
        print"Numero impar"
if var == "residuo":
    var11 = int (raw_input("Ingrese un numero: "))
    var12 = int (raw_input("Ingrese un numero: ")) 
    print "Residuo:", var11 % var12
    if var11%var12%2==0:
        print"Numero par"
    if var11%var12%2!=0:
        print"Numero impar"
