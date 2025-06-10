# dias = int(input("Cuantos dias desea ahorrar?: "))

# dinero = int(input(f"Cuanto dinero desea ahorrar cada dia?: "))

# total = 0

# for i in range(1, dias + 1):
#     total+=dinero
#     print(f"Llevas ahorrado este monto: {total}")

# print(f'''
# Resumen:
#       Decidiste ahorrar cada dia ${dinero} por {dias} dias.
#       Ahorraste finalmente: ${total}
# ''')

# total=0
# item=0
# ingreso_producto=int(input("Ingrese el precio del producto o un 0 para terminar: "))
# while ingreso_producto != 0:
#     total+=ingreso_producto
#     item+=1
#     print(f"Llevas {item} productos y un total de ${total}")
#     ingreso_producto=int(input("Ingrese el precio del producto o un 0 para terminar: "))
# if total >= 50000:
#     print("Felicitaciones al superar el total de 50000 usted gano un 10% de descuento")
#     print(f'''
# RESUMEN BOLETA:
#         TOTAL DE PRODUCTOS: {item}
#         TOTAL SIN DESCUENTO Y SIN IVA: ${total}
#         TOTAL FINAL: ${(total*1.19)*0.90}
# GRACIAS POR SU COMPRA!
# ''')
# else:
#     print(f'''
# RESUMEN BOLETA:
#         TOTAL DE PRODUCTOS: {item}
#         TOTAL SIN DESCUENTO Y SIN IVA: ${total}
#         TOTAL FINAL: ${total*1.19}
# GRACIAS POR SU COMPRA!
# ''')

# print("Bienvenido al parque de diversiones de python!")
# personas_si=0
# personas_no=0
# personas=0
# edades_si=0
# edades_gente = int(input("Ingrese las edades de la diferentes personas que queren ingresar o -1 para terminar: "))

# while edades_gente != -1:
#     if edades_gente >= 12 and edades_gente <= 60:
#         personas_si+=1
#         personas+=1
#         edades_si+=edades_gente
#         edades_gente = int(input("Ingrese las edades de la diferentes personas que queren ingresar: "))
#     else:
#         personas_no+=1
#         personas+=1
#         edades_gente = int(input("Ingrese las edades de la diferentes personas que queren ingresar: "))

# if personas_si > 0:
#     promedio = edades_si / personas_si
# else:
#     promedio = 0

# print(f'''
# Resumen:
#     Personas total: {personas}
#     Personas que lograron entrar: {personas_si}
#     Personas que no entraron: {personas_no}
#     Promedio de edades de los que entraron {promedio}
# ''')

# Juego

# Reglas o requisitos:
# Hay dos jugadores: Jugador y el boss.

# El jugador tiene 100 de vida.
# El jefe final tiene 150 de vida.

# Cada ronda:
# El jugador ataca primero:
# Elige entre 3 opciones:

# 1. Golpe rápido (10 de daño)

# 2. Golpe fuerte (25 de daño, pero con 50% de probabilidad)

# 3. Curarse (+15 de vida, máximo 100)

# Luego el jefe ataca y hace entre 10 y 20 de daño aleatorio al jugador.
# El juego muestra:
# Vida del jugador y del jefe después de cada ronda.
# Cuántas rondas han pasado.
# El combate sigue hasta que uno de los dos llegue a 0 o menos de vida.
# Al final, mostrar:
# Quién ganó.
# Cuántas rondas duró el combate.

# import random as rd
# import time as tm

# vida_pj=100
# vida_boss=150
# rondas=0

# turno="pj"
# print("Bienvenido al juego de tu puta madre digo python")
# print(f"Tienes {vida_pj} de vida y el boss tiene {vida_boss} de vida")
# while vida_pj > 0 and vida_boss > 0:
#     if turno == "pj":
#         while turno == "pj":
#             op=(int(input('''
# Que desea hacer?
#                           1. Golpe rapido (10 de dano)
#                           2. Golpe fuerte (25 de dano, pero con 50% de probabilidad)
#                           3. Curarse (+15 de vida, maximo 100)
#                           4. Saltar
# ''')))
#             match op:
#                 case 1:
#                     print("Le pegaste una cachetada a el boss")
#                     vida_boss-=10
#                     print(f"pj: {vida_pj}")
#                     print(f"boss: {vida_boss}")
#                     rondas+=1
#                     tm.sleep(2.0)
#                     turno = "boss"
#                 case 2:
#                     if rd.randint(1, 2) == 1:
#                         print("Le pegaste un combo a el boss")
#                         vida_boss-=25
#                         print(f"pj: {vida_pj}")
#                         print(f"boss: {vida_boss}")
#                         rondas+=1
#                         tm.sleep(2.0)
#                         turno = "boss"
#                     else:
#                         print("Fallaste")
#                         rondas+=1
#                         tm.sleep(2.0)
#                         turno = "boss"
#                 case 3:
#                     if vida_pj <= 85:
#                         print("Te has curado")
#                         vida_pj+=15
#                         print(f"pj: {vida_pj}")
#                         print(f"boss: {vida_boss}")
#                         rondas+=1
#                         tm.sleep(2.0)
#                         turno = "boss"
#                     else:
#                         print("No te puedes curar... que pena")
#                 case 4:
#                     print("Pasaste")
#                     rondas+=1
#                     tm.sleep(2.0)
#                     turno = "boss"
#                 case _:
#                     print("Opcion invalida")
#     else:
#         if rd.randint(1, 2) == 1:
#             dano=rd.randint(10,20)
#             print("El boss se enojo y te pego una patada")
#             print(f"Te hizo {dano} de dano")
#             vida_pj-=dano
#             print(f"pj: {vida_pj}")
#             print(f"boss: {vida_boss}")
#             tm.sleep(2.0)
#             turno="pj"
#         else:
#             print("El boss fallo")
#             tm.sleep(2.0)
#             turno="pj"
# if vida_boss <= 0:
#     print("Ganaste!")
#     print(f"Duro {rondas} rondas")
# else:
#     print("Perdiste...")
#     print(f"Duro {rondas} rondas")



# vida = 100
# nivel = 1

# import random as rd
# import time as tm

# print('''
# Bienvenido al laberinto de python!
# En total hay 5 niveles que superar y 3 puertas que pasar por cada uno de estos niveles...
# ''')

# while vida > 0 and nivel <= 5:
#     print(f"Nivel {nivel} ... Hay tres puertas frente a ti y debes pasar por una...")
#     puerta1=rd.randint(1,3)
#     op1=int(input('''
# Ingresa por una puerta...
#                     1. Puerta roja
#                     2. Puerta verde
#                     3. Puerta azul
# '''))
#     match op1:
#         case 1:
#             if puerta1 == op1:
#                 print("Lo pasaste sin problemas!")
#                 nivel+=1
#             else:
#                 print("Fallaste y te hiciste dano")
#                 dano=rd.randint(10,30)
#                 vida-=dano
#                 print(f"Te queda {vida} de vida")
#         case 2:
#             if puerta1 == op1:
#                 print("Lo pasaste sin problemas!")
#                 nivel+=1
#             else:
#                 print("Fallaste y te hiciste dano")
#                 dano=rd.randint(10,30)
#                 vida-=dano
#                 print(f"Te queda {vida} de vida")
#         case 3:
#             if puerta1 == op1:
#                 print("Lo pasaste sin problemas!")
#                 nivel+=1
#             else:
#                 print("Fallaste y te hiciste dano")
#                 dano=rd.randint(10,30)
#                 vida-=dano
#                 print(f"Te queda {vida} de vida")
# if nivel >= 5 and vida > 0:
#     print("Ganaste!")
# else:
#     print("Perdiste...")
import random as rd
import time as tm

vida = 100
dinero = 0
turno = "pj"


def pelea():
    global vida, dinero, turno, vida_cliente
    print("Combate iniciado!")
    vida_cliente=30
    while vida > 0 and vida_cliente > 0:
        if turno == "pj":
            ops=int(input('''
                        Que desea hacer?
                        1. Golpe rapido
                        2. Golpe fuerte (25% de chance)
                        3. comer helado (Te cura 10 pero gastas $10)
    '''))
            match ops:
                case 1:
                    print("Le diste una cachetada al cliente")
                    vida_cliente -= 10
                    print(f"Tienes {vida} de vida y el cliente {vida_cliente} de vida")
                    turno = "cliente"
                case 2:
                    chance=rd.randint(1,4)
                    if chance == 1:
                        print("Le pegaste un combo en el hocico")
                        vida_cliente -= 30
                        print(f"Tienes {vida} de vida y el cliente {vida_cliente} de vida")
                        turno = "cliente"
                    else:
                        print("Fallaste")
                        turno = "cliente"
                case 3:
                    if dinero > 10:
                        print("Comes helado :v")
                        vida+=10
                        dinero-=10
                        print(f"Gastas $10 y tienes ahora {dinero}")
                    else:
                        print("No tienes dinero...")
        else:
            dano=rd.randint(5,10)
            chance2=rd.randint(1,4)
            if chance2 == 1:
                print("El cliente fallo")
                turno = "pj"
            else:
                print(f"Te pego con el helado y te hizo {dano} de dano")
                vida-=dano
                print(f"tienes {vida} de vida y el cliente {vida_cliente} de vida")
                turno = "pj"
    if vida_cliente <= 0 and vida > 0:
        print("Plop Ganaste!")
        ganado=rd.randint(15,25)
        print(f"Ademas ganaste ${ganado} de dinero")
        dinero += ganado
    else:
        print("Plop Te Moriste bastardo manco...")


print("Bienvenido a la heladeria violenta, tu seras el heladero violento...")

while dinero <= 100 and vida > 0:
    cliente = rd.randint(1,5)
    if cliente == 1:
        print("El cliente se ve algo alterado...")
        op = int(input('''Que deseas hacer?
                    1. Vender helado por $10
                    2. Negociar para vender el helado a $15 o defenderte
                    3. Agarrarte a putazos (hay chance que te pague por el caos)
                    '''))
        match op:
            case 1:
                print("Le vendes el helado y te paga de mala gana los $10")
                dinero+=10
                print(f"Ganaste $10! ahora tienes en el banco: ${dinero}")
            case 2:
                print("Estas negociando...")
                tm.sleep(1.0)
                defensa=rd.randint(1,2)
                if defensa == 1:
                    print("Cagaste...")
                    pelea()
                else:
                    dinero+=15
                    print(f"Funciono! ganaste $15 y ahora tienes ${dinero}")
            case 3:
                pelea()
    else:
        print("El cliente se ve amable...")
        op=int(input('''Que deseas hacer?
                    1. Vender helado por $20
                    2. Negociar para vender el helado a $25 o defenderte
                    3. Agarrarte a putazos (hay chance que te pague por el caos)
                    '''))
        match op:
            case 1:
                print("Le vendes el helado y te paga $20")
                dinero+=20
                print(f"Ganaste $20! ahora tienes en el banco: ${dinero}")
            case 2:
                print("Estas negociando...")
                tm.sleep(2.0)
                defensa=rd.randint(1,2)
                if defensa == 1:
                    print("Cagaste...")
                    pelea()
                else:
                    dinero+=25
                    print(f"Funciono! ganaste $25 y ahora tienes ${dinero}")
            case 3:
                pelea()
if dinero >= 100 and vida > 0:
    print("Ganaste y se cerro el boliche")
else:
    print("Vales vrga")




