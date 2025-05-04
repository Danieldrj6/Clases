# Ejercicios
"""
clave=1234
password=int(input("Ingrese la clave: "))
while clave!=password:
    print("Error; clave invalidad")
    password=int(input("Ingrese la clave: "))
print("Bienvenido al sistema")
"""
"""
clave=1234
intentos=1
password=int(input("Ingrese la clave: "))
while clave!=password and intentos<=3:
    print("Error clave invalida")
    password=int(input("Ingrese la clave: "))
print("Bienvenido al sistema")
"""

import random as rd
"""
total=0
num=rd.randint(1,30)
total=total=num
print(F"Tienes un total de: {total} y te salio: {num}")
print("Necesitas 20 puntos justo para ganar!")
if total<20:
    print("Te falta puntaje")
elif total>20:
    print("Te pasaste")
else:
    print("Ganaste!")
"""

# num=rd.randint(1,50)
# print(num)
# usuario=int(input("Ingrese un numero: "))
# while usuario<num:
#     print("Tu numero es menor al que debes adivinar")
#     usuario=int(input("Ingrese un numero: "))
# while usuario>num:
#     print("Tu numero es mayor al que debes adivinar")
#     usuario=int(input("Ingrese un numero: "))
# print(F"Adivinaste! el numero era {num}")

# barril=rd.randint(1,6)
# print(barril)
# rul=int(input("Ingrese un numero de vueltas al revolver: "))
# print("disparaste y...")
# while rul!=barril:
#     print("No paso nada...")
#     rul=int(input("Ingrese un numero de vueltas al revolver: "))
# print("Disparaste y...")
# print("BANG!")

import time as tm

# meta=30
# turno=1
# j1=1
# j2=1
# while j1<30 and j2<30:
#     print(F"Jugador 1 en la casilla {j1} y jugador 2 en la casilla {j2}")
#     if turno % 2==0:
#         print("Turno de jugador 1")
#         dado=rd.randint(1,6)
#         j1=j1+dado
#         tm.sleep(1)
#         print(F"Jugador 1 saco {dado}")
#         print(F"Avanza hasta la casilla {j1}")
#     else:
#         print("Turno del jugador 2")
#         dado=rd.randint(1,6)
#         j2=j2+dado
#         tm.sleep(1)
#         print(F"Jugador 2 saco {dado}")
#         print(F"Avanza hasta la casilla {j2}")
# if j1>=30:
#     print("Jugador 1 gana!")
# else:
#     print("Jugador 2 gana!")

# arancel=200000
# descuento=0

# print('''
#       comunas disponibles:
#     1. La florida = 20%
#     2. La Pintana = 20%
#     3. Puente Alto = 25%
#     4 San Juaquin = 15%
# ''')

# grupo_familiar=int(input("Ingrese su grupo familiar: "))

# if grupo_familiar==1:
#     grupo_familiar=2
# elif grupo_familiar<4 and grupo_familiar>2:
#     grupo_familiar=3
# else:
#     grupo_familiar=4

# comuna=int(input("Ingrese numero de su comuna: "))

# if comuna==1:
#     comuna=20

# elif comuna==2:
#     comuna=20

# elif comuna==3:
#     comuna=25

# elif comuna==4:
#     comuna=15
# else:
#     print("Error opcion invalida")

# descuento=grupo_familiar+comuna
# descuento_total=(descuento*arancel)/100
# descuento_final=arancel-descuento_total
# print(F"Usted debe pagar {descuento_final}")

