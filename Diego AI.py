# -*- coding: utf-8 -*-
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
lista7 = []

lista8 = ["hola", "como estas?", "que haces?", "bien", "ya te dije"]
lista9 = ["Hola!" "que tal!", "bien y tu?", "charlo contigo!", "me alegra", "no sabia"]
activo = True
seguir = True
palabra = str
a=0


print "Hola soy Diego"
nombre = str (raw_input("Cual es tu nombre?: "))
print ""
print "Encantado de conocerte", nombre,"!"

while activo == True:
    print "--------------------------------------------------------"
    var = str (raw_input("Pideme algo: "))

    if var == "charlemos":
        print ""
        print "Si quieres parar de charlar solo di: *paremos de charlar*"
        while seguir == True:
            print ""
            charla = str (raw_input("Dime algo: "))
            if charla == "paremos de charlar":
                seguir = False
                break
            for i in range (len(lista8)):
                if lista8[i] == charla:
                    palabra = charla
                    break
            if palabra == charla:
                print "-",lista9[i]
                print "--------------------------------------------------------"
            if palabra != charla:
                lista8.append(charla)
                print "Disculpa no te he entendido"
                nuevo = str (raw_input("Que se supone que deba responder a eso?: "))
                print ""
                lista9.append(nuevo)
                print "Gracias a ti ya he aprendido algo nuevo!"
                print "--------------------------------------------------------"
        
        
    if var == "que puedes hacer?" and "que puedo hacer?":
        print ""
        print "--------------------------------------------------------------"
        print "Puedo:"
        print "1. Calcular operaciones, solo di: calcula"
        print "2. Charlar contingo, solo di: charlemos"
        print "3. Recordarte datos, solo di: recuerdame"
        print "4. Decirte lo que me pediste que recordara: (recuerdame las personas),"
        print "(recuerdame mis citas), (dime mis recordatorios)"
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

    if var == "recuerdame las personas":            
        print "--------------------------------------------------------------"
        print "Tengo a las siguientes personas notadas en mi cuaderno:"
        for i in range (len(lista1)):
            a=a+1
            print a,"-",lista1[i]
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

    if var == "ciencia":
        print "--------------------------------------------------------------"
        print "Que tipo de ecuaciones deseas resolver?"
        ciencia = str (raw_input("(relatividad, mecanica cuantica, movimiento, termodinamica): "))
        if ciencia == "relatividad":
            print "--------------------------------------------------------------"
            print "Cual ecuacion quieres resolver?"
            relatividad = str (raw_input("(dilatacion temporal, contraccion de lorentz, radio de Schwarchirdz): "))
            if relatividad == "dilatacion temporal":
                print ""
                t = float (raw_input("Tiempo de observador en reposo en horas: "))
                v = float (raw_input("Velocidad del observador en movimiento en km/s: "))
                c = float (300000.0)
                var = 0
                var=v/c
                var=var*var
                var=1-var
                p=var
                i=0
                while i!=p:
                    i=p
                    p=(var/p+p)/2
                    resul=t*p
                print "A", v,"km/s", t, "horas terraqueas se perciben como", resul, "horas."
                var= 0
                resul = 0
                t= 0
                v= 0
                c= 0
            if relatividad == "contraccion de lorentz":
                print ""
                l = float (raw_input("Longitud de observador en reposo en metros: "))
                v = float (raw_input("Velocidad del observador en movimiento en km/s: "))
                c = float (300000.0)
                var = 0
                resul=0
                var=(v*v)/(c*c)
                var=1-var
                p=var
                i=0
                while i!=p:
                    i=p
                    p=(var/p+p)/2
                    resul=l*p
                print "A", v, "km/s", l, "metros terraqueas se perciben como", resul, "metros."
                var= 0
                resul = 0
                l= 0
                v= 0
                c= 0
                

    if var == "chao" and "adios" and "nos vemos" and "vemos" and "hasta luego":
        activo=False

print "Hasta luego, si necesitas algo mas no dudes en buscarme!"
adios = str (raw_input("Di: salir "))
