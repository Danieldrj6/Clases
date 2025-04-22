# for i in range(1, 11):
#     print("Esta es la tabla del ", i)
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

# cant=int(input("Ingrese cantidad de repeticiones: "))
# for i in range(cant):
#     print("Esta es la tabla del ", i)
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

# nombre=str(input("Ingrese su nombre: "))
# edad=int(input("Ingrese su edad: "))
# print(F"Hola {nombre} su edad es {edad}")

# num=int(input("Ingrese un numero para ver su tabla de multiplicar: "))

# for i in range(1,11):
#     print(i, "x", num, "=", i*num)

# cant=int(input("Ingrese cantidad de notas"))
# total=0

# for i in range(cant):
#     print("Ingrese la nota ", i+1)
#     nota=float(input())
#     total=total+nota
# prom=total/cant
# print(F"Tu promedio es: {round(prom)}")

# if prom >= 4:
#     print("Aprobado")
# else:
#     print("Reprobado")

# clave="1234"

# passw=input("Ingrese la clave: ")
# if passw == clave:
#     print("Bienvenido al sistema")
# else:
#     print("Clave incorrecta")

cant=int(input("Cuantos productos llevara?"))
total=0

for i in range(cant):
    print(
        "Que productos llevara? " \
        " 1. Rifle " \
        " 2. Sniper " \
        " 3. Escopeta " \
        " 4. Bazooka " 
    )
    opcion=input()
    if opcion == "1":
        print("El precio del rifle es 5000")
        total=total+5000
        print("LLevaste un rifle y tienes un total de ", total)
    elif opcion == "2":
        print("El precio del sniper es 10000")
        total=total+10000
        print("LLevaste un sniper y tienes un total de ", total)
    elif opcion == "3":
        print("El precio de la escopeta es de 3000")
        total=total+3000
        print("LLevaste una escopeta y tienes un total de ", total)
    elif opcion == "4":
        print("El precio de una bazooka es de 20000")
        total=total+20000
        print("Llevaste una bazooka y tienes un total de ", total)
    else:
        print("Opcion no valida")
        break
    