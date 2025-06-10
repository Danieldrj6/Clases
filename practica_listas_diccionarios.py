# import random as rd
# import time as tm

# Inventario = {
#     "pocion": 3,
#     "oro": 100,
#     "Espadas": 1
# }

# objetos = {"gema": 15,
#            "llave": 5,
#            "reliquia": 25,
#            "piedra magica": 20,
#            "mapa": 10,
#            "pocion rara": 18
#            }

# mochila = ["llave", "gema"]

# while True:  
#     opciones=int(input('''Ingrese una opcion: 
#                    1. Usar pocion
#                    2. Recoger objeto
#                    3. Vender objeto
#                    4. Mostrar inventario
#                    5. Mostrar mochila
#                    6. Salir
#                    '''))
#     match opciones:
#         case 1:
#             if Inventario["pocion"] > 0:
#                 Inventario["pocion"]-= 1
#                 print(f"Usaste una pocion. Te quedan {Inventario['pocion']}")
#         case 2:
#             objeto_nuevo = rd.choice(list(objetos.keys()))
#             print(f"Encontraste un(a) {objeto_nuevo} y lo guardaste en tu mochila")
#             mochila.append(objeto_nuevo)
#         case 3:
#             print("Que objeto desea vender?")
#             for nombre, valor in objetos.items():
#                 print(f"{nombre} -> {valor} oro")
#         case 4:
#             for objetos_inv in Inventario:
#                 print(objetos_inv, "->", Inventario[objetos_inv])
#         case 5:
#             for nombre in objetos.items():
#                 print("")
#         case 6:
#             print("Saliendo...")
#             break

# Explicacion de diccionarios y listas

# Practica

import time as tm
import random as rd

print("Bienvenido al juego del gato Missy ninja robadora de jamones")
print("Tu objetivo es robar 20 jamones y no perder todas tus vidas")
jamon = 0
vida = 7
def casa():
    global jamon, vida
    global casas, situacionesabuela, situacionesvecino, situacionamigo, situaciondesconocido
    casas = ["Casa de la abuela", "Casa del vecino", "Casa del amigo", "Casa del desconocido"]
    situacionesabuela = ["Encontraste un jamon", "No hay nada", "No hay nada", "Encontraste un perro guardián", "Te pego con la chancla la abuela", "Te pego con la chancla la abuela", "Te pego con la chancla la abuela"]
    situacionesvecino = ["Encontraste un jamon", "Encontraste un jamon", "No hay nada", "No hay nada" "Encontraste un gato guardián", "Encontraste dos jamones", "Encontraste una trampa", "Encontraste una trampa"]
    situacionamigo = ["Encontraste un jamon", "Encontraste un jamon", "Encontraste un jamon", "No hay nada", "Encontraste dos jamones", "El compa te pateo el trasero", "El compa te pateo el trasero"]
    situaciondesconocido = ["Te pego con una chancla", "Te robo un jamon", "Te robo un jamon", "Te robo un jamon", "Te dio un jamon", "No hay nada"]
    casarandom = rd.choice(casas)
    print(f"Has entrado a la {casarandom}")
    if casarandom == "Casa de la abuela":
        opabuela = int(input('''
        Que desea hacer?
          1. Robar jamon
          2. Salir de la casa
'''))
        match opabuela:
            case 1:
                situacionesrandom = rd.choice (situacionesabuela)
                match situacionesrandom:
                    case "Encontraste un jamon":
                        print("Has encontrado un jamon! ahora tienes", jamon + 1)
                        jamon += 1
                    case "No hay nada":
                        print("No hay nada en la casa")
                    case "Encontraste un perro guardián":
                        print("Has encontrado un perro guardián, te ha mordido y has perdido 1 de vida ahora tienes", vida - 1)
                        vida -= 1
                    case "Te pego con la chancla la abuela":
                        print("La abuela te ha pegado con la chancla, has perdido 1 de vida ahora tienes", vida - 1)
                        vida -= 1
            case 2:
                print("Has salido de la casa de la abuela")
                return
            case _:
                print("Opción no válida, intenta de nuevo")
                casa()
    elif casarandom == "Casa del vecino":
        opvecino = int(input('''
        Que desea hacer?
          1. Robar jamon
          2. Salir de la casa
'''))
        match opvecino:
            case 1:
                situacionesrandom = rd.choice(situacionesvecino)
                match situacionesrandom:
                    case "Encontraste un jamon":
                        print("Has encontrado un jamon! ahora tienes", jamon + 1)
                        jamon += 1
                    case "No hay nada":
                        print("No hay nada en la casa")
                    case "Encontraste un gato guardián":
                        print("Has encontrado un gato guardián, te ha arañado salvajemente y has perdido 1 de vida ahora tienes", vida - 1)
                        vida -= 1
                    case "Encontraste dos jamones":
                        print("Has encontrado dos jamones! ahora tienes", jamon + 2)
                        jamon += 2
                    case "Encontraste una trampa":
                        print("Has caído en una trampa, has perdido 1 de vida ahora tienes", vida - 1)
                        vida -= 1
            case 2:
                print("Has salido de la casa del vecino")
                return
            case _:
                print("Opción no válida, intenta de nuevo")
                casa()
    elif casarandom == "Casa del amigo":
        opamigo = int(input('''
        Que desea hacer?
          1. Robar jamon
          2. Salir de la casa
'''))
        match opamigo:
            case 1:
                situacionesrandom = rd.choice(situacionamigo)
                match situacionesrandom:
                    case "Encontraste un jamon":
                        print("Has encontrado un jamon! ahora tienes", jamon + 1)
                        jamon += 1
                    case "No hay nada":
                        print("No hay nada en la casa")
                    case "Encontraste dos jamones":
                        print("Has encontrado dos jamones! ahora tienes", jamon + 2)
                        jamon += 2
                    case "El compa te pateo el trasero":
                        print("El compa te ha pateado el trasero, has perdido 2 de vida ahora tienes", vida - 2)
                        vida -= 2
                    case 2:
                        print("Has salido de la casa del amigo")
                        return
                    case _:
                        print("Opción no válida, intenta de nuevo")
                        casa()
    elif casarandom == "Casa del desconocido":
        opdesconocido = int(input('''
        Que desea hacer?
          1. Robar jamon
          2. Salir de la casa
'''))
        match opdesconocido:
            case 1:
                situacionesrandom = rd.choice(situaciondesconocido)
                match situacionesrandom:
                    case "Te pego con una chancla":
                        print("El desconocido te ha pegado con una chancla, has perdido 2 de vida ahora tienes", vida - 2)
                        vida -= 1
                    case "Te robo un jamon":
                        if jamon <= 0:
                            print("No tienes jamones para robar")
                        else:
                            print("El desconocido te ha robado un jamon, has perdido 1 de jamon ahora tienes", jamon - 1)
                            jamon -= 1
                    case "Te dio un jamon":
                        print("El desconocido te ha dado un jamon! ahora tienes", jamon + 1)
                        jamon += 1
                    case "No hay nada":
                        print("No hay nada en la casa")
            case 2:
                print("Has salido de la casa del desconocido")
                return
            case _:
                print("Opción no válida, intenta de nuevo")
                casa()

while jamon < 20 and vida > 0:
    op = int(input('''
        Que desea hacer?
          1. Entrar a una casa random
          2. Ver jamones totales
          3. Comer jamon para curarte
'''))
    match op:
        case 1:
            casa()
        case 2:
            print(f"Tienes {jamon} jamones")
        case 3:
            if jamon > 0:
                print("Comiendo jamon...")
                tm.sleep(2)
                print("Has comido un jamon y te has curado 1 de vida ahora tienes", vida + 1) 
                jamon -= 1
                vida += 1
            else:
                print("No tienes jamones para comer")
        case _:
            print("Opción no válida, intenta de nuevo") 
    if vida <= 0:
        print("Has perdido todas tus vidas, el juego ha terminado")
        print("Gracias por jugar al juego del gato ninja robador de jamones")
        break
if jamon >= 20:
    print("Felicidades, eres gay! digo, has robado 20 jamones y has ganado el juego")
    print("Gracias por jugar al juego del gato ninja robador de jamones")

            