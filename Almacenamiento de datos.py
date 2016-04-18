# -*- coding: utf-8 -*-
lista1 = []
lista2 = []
i = len(lista1)
p = len(lista2)
var5=True
var7 = True
var9= int (0)
var11 = True

print"Datos"
print ""

while var7==True:
    var = int (raw_input("Cuantas personas desea anadir?: "))
    print "-------------------------------------"
    var9=var9+var
    while len(lista1) != var9:
        var1 = str (raw_input("Nombre: "))
        lista1.append(var1)
        var2= int (raw_input("Edad: "))
        lista2.append(var2)
        print ""
        print "Usted ha agredado", len(lista1), "persona(s)"
        print "-------------------------------------"
        
    var= int(0)
    print "Ha terminado de agregar personas"
    print ""
    var3 = str (raw_input("Desea revisar los datos de alguna persona?: "))
    print ""

    if var3 == "si":
        while var5 == True:
            print "Inserte un numero del 1 -", len(lista1)
            var4 = int (raw_input("Insertelo aqui: "))
            var4 = var4-1
            print ""
            print "--------------------------------------"
            print "Nombre:", lista1[var4]
            print "Edad:", lista2[var4]
            print "--------------------------------------"
            var6 = str (raw_input("Desea revisar los datos de otra persona?: "))
            print ""
            if var6 == "no":
                var5=False
                
    var10 = str (raw_input("Desea editar los datos de alguna persona?: "))
    print ""

    if var10 == "si":
        while var11 == True:
            print "Inserte un numero del 1 -", len(lista1)
            var14 = int (raw_input("Insertelo aqui: "))
            var14 = var14-1
            print ""
            print "--------------------------------------"
            print "Nombre:", lista1[var14]
            print "Edad:", lista2[var14]
            print "--------------------------------------"
            var12 = str (raw_input("Ingrese el nuevo nombre: "))
            var13 = int (raw_input("Ingrese la nueva edad: "))
            lista1[var14]=var12
            lista2[var14]=var13
            print "--------------------------------------"
            print "La informacion ha cambiado a: "
            print "Nombre:", lista1[var14]
            print "Edad:", lista2[var14]
            print "--------------------------------------"
            var15 = str (raw_input("Desea editar los datos de otra persona?: "))
            print ""
            if var15 == "no":
                var11=False
    var8 = str(raw_input("Desea agregar mas personas?: "))
    print ""
    if var8 == "no":
        var7=False
print ""
print ""
print "Gracias por usar nuestro servicio"
var16 = str(raw_input("Desea cerrar el programa?: "))
        
                


            
        

    
    
    
    

