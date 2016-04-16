lista1 = []
continuar=True


while continuar==True:
    n=int(raw_input("Ingrese: "))
    lista1.append(n)
    print "Posee", len(lista1), "datos"
    i= str (raw_input("Desea continuar? (Si, No): "))
    if i=="si":
        continuar=True
    if i=="no":
        continuar=False
print "Sus datos son", lista1
p=len(lista1)
mayor=0
for i in range (p):
    if lista1[i] > mayor:
        mayor = lista1[i]
print "El numero mayor es", mayor
        
        

    
