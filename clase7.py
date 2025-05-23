import random as rd
fallidos=0
logrados=0
while True:
    try:
        perros=int(input("Ingrese cantidad de perros de caza que se van a utilizar: "))
        break
    except Exception:
        print("No es un numero valido")
while True:
    try:
        conejos=int(input("Ingrese el minimo de conejos que deberian traer cada perro: "))
        break
    except Exception:
        print("No es un numero valido")

for i in range(1, perros+1):
    cazados=rd.randint(1,conejos+1)
    print(f"El perro {i} trajo {cazados} conejos")
    if cazados < conejos:
        print(f"El perro {i} se quedo sin filete de premio")
        fallidos+=1
    else:
        print(f"El perro {i} cumplio con la cuota minima por ello si tendra filete")
        logrados+=1

print(f"Hubieron {logrados} perros que lograron la cuota minima mientras que hubieron {fallidos} perros que no lo lograron")

