lista1 = []
n=0
continuar=True

while continuar == True:
    var = int (raw_input("Ingrese numero 1: "))
    var1 = int (raw_input("Ingrese numero 2: "))
    var1 = var1+1

    while var != var1:
        lista1.append(var)
        var = var+1

    for i in range (len(lista1)):
        n=n+lista1[i]
    print "-------------------------------------"
    print n
    print "-------------------------------------"
    n=0
    lista1=[]
    print ""
    seguir = str (raw_input("Desea continuar?: "))
    print ""
    if seguir == "no":
        continuar = False

adios = str (raw_input("Hasta luego"))
        



