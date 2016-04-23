# -*- coding: utf-8 -*-
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
lista7 = []
activo = True

print "Hola soy Diego"
nombre = str (raw_input("Cual es tu nombre?: "))
print ""
print "Encantado de conocerte", nombre,"!"

while activo == True:
    var = str (raw_input("Dime o pideme algo: "))
    
    if var == "hola":
        print ""
        print "--------------------------------------------------------------"
        print "Hola! Que chevere hablar contigo", nombre, "!"
        print "--------------------------------------------------------------"
        print ""
        
    if var == "algo":
        print ""
        print "--------------------------------------------------------------"
        print "Eso no es un tema de conversacion", nombre, ":V"
        print ""
        print "--------------------------------------------------------------"
        
    if var == "que puedes hacer?" and "que puedo hacer?":
        print ""
        print "--------------------------------------------------------------"
        print "Puedo:"
        print "1. Calcular operaciones, solo di: calcula"
        print "2. Charlar contingo"
        print "3. Recordarte datos, solo di: recuerdame"
        print "4. Decirte lo que me pediste que recordara: (recuerdame las personas),"
        print "(recuerdame mis citas), (dime mis recordatorios)"
        print "--------------------------------------------------------------"
        print ""
        
    if var == "que haces?":
        print ""
        print "--------------------------------------------------------------"
        print "Esperando a resolver tus necesidades", nombre
        print "--------------------------------------------------------------"
        print ""

    if var == "como estas?":
        print ""
        print "--------------------------------------------------------------"
        print "Bien gracias, algo cansado"
        print "--------------------------------------------------------------"
        print ""

    if var == "te amo":
        print ""
        print "--------------------------------------------------------------"
        print "Yo no, no mentiras <3"
        print "--------------------------------------------------------------"
        print ""

    if var == "quien creo el universo?":
        print ""
        print "--------------------------------------------------------------"
        print "Stephen Hawking"
        print "--------------------------------------------------------------"
        print ""
        
    if var == "quien te creo?":
        print ""
        print "--------------------------------------------------------------"
        print "Un crack llamado Daniel Reyes"
        print "--------------------------------------------------------------"
        print ""
        
    if var == "calcula":
        operacion = True
        while operacion == True:
            print ""
            print "--------------------------------------------------------------"
            print "Que operacion deseas hacer?"
            calcula = str (raw_input("(suma, resta, multiplicacion, division, residuo): "))
            if calcula == "suma":
                print ""
                a1 = int (raw_input("Ingresa un numero: "))
                a2 = int (raw_input("Ingresa un numero: "))
                print "Suma:", a1+a2
                print "--------------------------------------------------------------"
                print ""
            if calcula == "resta":
                print ""
                a3 = int (raw_input("Ingresa un numero: "))
                a4= int (raw_input("Ingresa un numero: "))
                print "Resta:", a3-a4
                print "--------------------------------------------------------------"
                print ""
            if calcula == "multiplicacion":
                print ""
                a5 = int (raw_input("Ingresa un numero: "))
                a6 = int (raw_input("Ingresa un numero: "))
                print "Multiplicacion:", a5*a6
                print "--------------------------------------------------------------"
                print ""
            if calcula == "division":
                print ""
                a7 = int (raw_input("Ingresa un numero: "))
                a8 = int (raw_input("Ingresa un numero: "))
                print "Division:", a7/a8
                print "--------------------------------------------------------------"
                print ""
            if calcula == "residuo":
                print ""
                a9 = int (raw_input("Ingresa un numero: "))
                a10 = int (raw_input("Ingresa un numero: "))
                print "Residuo:", a9%a10
                print "--------------------------------------------------------------"
                print ""
            continuar = str (raw_input("Deseas hacer otra operacion?: "))
            print ""
            if continuar == "no":
                operacion = False
        
    if var == "recuerdame":
        print ""
        print "--------------------------------------------------------------"
        recordar = str (raw_input("Que te recuerdo?: (personas), (citas), (recordatorios) "))
        if recordar == "personas":
            print ""
            print ""
            var1 = str (raw_input("Nombre: "))
            lista1.append(var1)
            var2= int (raw_input("Edad: "))
            lista2.append(var2)
            print ""
            print "He guardado satisfactoriamente tus datos", nombre
            print "Pideme que te diga los datos de esta persona diciendo: (recuerdame las personas)"
            print "--------------------------------------------------------------"
            print ""
        if recordar == "citas":
            print ""
            var3 = str (raw_input("Lugar: "))
            lista3.append(var3)
            var4= int (raw_input("Hora (1-24 horas): "))
            lista4.append(var4)
            var5= str (raw_input("Tema: "))
            lista5.append(var5)
            print ""
            print "He guardado satisfactoriamente tus datos", nombre
            print "Pideme que te recuerde tu cita diciendo: (recuerdame mis citas)"
            print "--------------------------------------------------------------"
            print ""
        if recordar == "recordatorios":
            print ""
            var6 = str (raw_input("Tema: "))
            lista6.append(var6)
            var7 = str (raw_input("Dia (lunes, martes, miercoles, jue...): "))
            lista7.append(var7)
            print ""
            print "He guardado satisfactoriamente tus datos", nombre
            print "Pideme que te recuerde tu cita diciendo: (dime mis recordatorios)"
            print "--------------------------------------------------------------"
            print ""
    
    if var == "quien es Stephen Hawking?":
        print "--------------------------------------------------------------"
        print "Es Dios"
        print "--------------------------------------------------------------"

    if var == "recuerdame las personas":
        print "--------------------------------------------------------------"
        print "Tengo", len(lista1), "anotadas en mi cuaderno"
        print "Cual te recuerdo (1-", len(lista1), ")?"
        gente = int (raw_input(""))
        gente = gente-1
        print ""
        print "Nombre:", lista1[gente]
        print "Edad:", lista2[gente]
        print "--------------------------------------------------------------"
        gente= int (0)
        
    if var == "recuerdame mis citas":
        print "--------------------------------------------------------------"
        print "Tengo", len(lista3), "citas anotadas en mi cuaderno"
        print "Cual te recuerdo (1-", len(lista3),")?"
        citas = int (raw_input(""))
        citas = citas-1
        print ""
        print "Lugar:", lista3[citas]
        print "Hora:", lista4[citas], "horas del dia"
        print "Tema:", lista5[citas]
        print "--------------------------------------------------------------"
        gente = int (0)

    if var == "dime mis recordatorios":
        print "--------------------------------------------------------------"
        print "Tengo", len(lista6), "recordatorios anotados en mi cuaderno"
        print "Cual te recuerdo (1-", len(lista6),")?"
        recordatorios = int (raw_input(""))
        recordatorios = recordatorios-1
        print ""
        print "Tema:", lista6[recordatorios]
        print "Dia:", lista7[recordatorios]
        print "--------------------------------------------------------------"
        recordatorios = int (0)

    if var == "chao" and "adios" and "nos vemos" and "vemos" and "hasta luego":
        activo=False

print "Hasta luego, si necesitas algo mas no dudes en buscarme!"
adios = str (raw_input("Di: salir "))
