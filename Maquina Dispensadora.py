# -*- coding: utf-8 -*-
print "Maquina dispensadora"
var = int(raw_input("Ingrese el dinero: "))
if var<200:
    print "Ingrese una cantidad entre 200 y 2500"
    print var, "pesos han sido devueltos" 
    print "Intentelo de nuevo"
    import sys
    sys.exit("Intentelo de nuevo")
if var>2500:
    print "Ingrese una cantidad entre 200 y 2500"
    print var, "pesos han sido devueltos" 
    print "Intentelo de nuevo"
    import sys
    sys.exit("Intentelo de nuevo")
print "Ha insertado", var, "pesos"
print "Aqui esta el menu: "
print "1. Papas Fritas $1200"
print "2. Sandwich Combinado $2500"
print "3. Pescadito $1800"
print "4. Empanada $1700"
print "5. Arepa $2000"
print "6. Gaseosa $1600"
print "7. Vaso de Te $1000"
print "8. Dulce $200"
print "9. Salir"
var2 = int(raw_input("Digite su opcion: "))

if var2 == 1:
    if var<= int (1199):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (1200):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-1200, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-1200)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-1200)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-1200)%200)/devolucion), "monedas de 100 pesos"
            
if var2 == 2:
    if var<= int (2499):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (2500):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-2500, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-2500)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-2500)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-2500)%(200))/devolucion), "monedas de 100 pesos"

if var2 == 3:
    if var<= int (1799):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (1800):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-1800, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-1800)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-1800)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-1800)%(200))/devolucion), "monedas de 100 pesos"

if var2 == 4:
    if var<= int (1699):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (1700):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-1700, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-1200)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-1200)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-1200)%200)/devolucion), "monedas de 100 pesos"

if var2 == 5:
    if var<= int (1999):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (2000):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-2000, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-1200)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-1200)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-1200)%200)/devolucion), "monedas de 100 pesos"

if var2 == 6:
    if var<= int (1599):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (1600):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-1600, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-1200)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-1200)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-1200)%200)/devolucion), "monedas de 100 pesos"

if var2 == 7:
    if var<= int (999):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (100):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-1000, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-1200)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-1200)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-1200)%200)/devolucion), "monedas de 100 pesos"

if var2 == 8:
    if var<= int (199):
        print "No ingreso el dinero suficiente para este producto"
        print var, "han sido devueltos" 
        print "Intentelo de nuevo"
        import sys
        sys.exit("Intentelo de nuevo")
    if var>= int (200):
        print "Gracias por adquirir el producto"
        print "Se le seran devueltos:", var-200, "pesos"
        for devolucion in  [500]:
            print "Recoja", ((var-1200)/devolucion), "monedas de 500 pesos"
        for devolucion in  [200]:
            print "Recoja", (((var-1200)%500)/devolucion), "monedas de 200 pesos"
        for devolucion in  [100]:
            print "Recoja", (((var-1200)%200)/devolucion), "monedas de 100 pesos"

if var2 == 9:
    print "Usted ha salido"
    print "Se le fueron devueltos", var
    import sys
    sys.exit("Usted ha salido")
        

