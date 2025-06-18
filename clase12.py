# notas = []

# while True:
#     op=int(input('''
#     Seleccione una opcion:
#         1. Ingresar notas
#         2. borrar nota
#         3. mostrar notas
#         4. sacar promedio, nota mayor y menor
#         5. limpiar lista de notas
#         6. salir
# '''))
#     match op:
#         case 1:
#             cant_notas=int(input("Ingrese cantidad de notas a ingresar: "))
#             for i in range(cant_notas):
#                 nota_extra=float(input(f"Ingrese nota {i+1}: "))
#                 notas.append(nota_extra)
#         case 2:
#             c=0
#             for nota in notas:
#                 print("opcion:",(c+1), " ", notas[c])
#                 c+=1
#             nota_borrar=int(input("Que nota desea borrar?: "))
#             notas.pop(nota_borrar-1)
#         case 3:
#             for nota in notas:
#                 print(nota)
#         case 4:
#             c=0
#             suma=0
#             for nota in notas:
#                 suma=suma+nota
#                 c+=1
#             prom=suma/len(notas)
#             print(prom)
#             nota_alta = max(notas)
#             nota_baja = min(notas)
#             print(f"La nota mas alta es: {nota_alta} y la mas baja es {nota_baja}")
#         case 5:
#             notas.clear()
#             print("Notas borradas!")
#         case 6:
#             print("Saliendo")
#             break

# diccionario = {
#     "nombre":"Daniel del rio jara",
#     "numero":932445769,
#     "casado":True
# }
# print(diccionario)
# for datos, valor in diccionario.items(): #.items para ver los items o valores
#     print(datos,valor)

# diccionario["edad"]=20
# diccionario["edad"]=int(input("Ingrese edad: "))
# print(diccionario)
# for datos, valor in diccionario.items(): #.items para ver los items o valores
#     print(datos,valor)

# diccionario_lista = {
#     "nombre":["Daniel", "Jose"],
#     "fonos": [932445769,988443322]
# }
# print(diccionario_lista)
# for datos2, valor2 in diccionario_lista.items():
#     print(datos2, valor2)

frutas = {}
precio=0

while True:
    op=int(input('''Ingrese opcion:
                 1. Ingresar fruta y precio
                 2. actualizar precio
                 3. borrar fruta y precio
                 4. mostrar todo
                 5. comprar
                 6. salir
'''))
    
    match op:
        case 1:
            fruta=input("ingrese fruta: ")
            frutas[fruta]=input("Ingrese precio: ")
            print(f"Tienes esto en frutas ingresadas: {frutas}")
        case 2:
            c=0
            for frutass in frutas.items():
                print("opcion", {c+1}, frutas)
                c+=1
            fruta_select=int(input("Ingrese fruta a actualizar: "))
            frutas[fruta_select-1]=input("Ingrese nuevo precio: ")
            print(f"Tiene esto actualmente: {frutas}")
        case 3:
            c=0
            for frutass in frutas.items():
                print("opcion", {c+1}, frutas)
                c+=1
            fruta_select=input("Ingrese fruta a borrar: ")
            frutas.pop[fruta_select]
            print(f"Tiene esto actualmente: {frutas}")
        case 4:
            for frutass in frutas.items():
                print(frutas)
                c+=1
        case 5:
            for frutass in frutas.items():
                
                print(precio)
        case 6:
            break


