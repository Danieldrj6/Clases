
# menu:
# Mostrar catálogo
# Mostrar juego más caro
# Actualizar precio
# Eliminar un juego
# Agregar nuevo juego
# Salir

juegos = {
    'J001': ['The Last of Us', 'PlayStation', 2013],
    'J002': ['Halo Infinite', 'Xbox', 2021],
    'J003': ['Zelda BOTW', 'Nintendo Switch', 2017]
}

precios = {
    'J001': [4, 25000],
    'J002': [2, 40000],
    'J003': [0, 35000],
    'J999': [1, 15000] #Este no existe
}

def mostrar():
    for ids, juego in juegos.items():
        print(f"Juego ID: {ids} {juego[0]} de la consola {juego[1]} con fecha del {juego[2]} con precio: {precios[ids][1]} y cantidad de stock: {precios[ids][0]}")

def precio(ids):
    return precios[ids][1]

def caro():
    juego_caro = max(precios, key=precio)
    print(f"El juego mas caro es el: {juegos[juego_caro][0]} con valor de ${precios[juego_caro][1]}")

def actualizar_precio():
    mostrar()
    seleccion = input("Ingrese el ID del juego a actualizar precio: ")
    if seleccion in precios:
        precio_nuevo = int(input("Ingrese precio nuevo: "))
        precios[seleccion][1] = precio_nuevo
        mostrar()
    else:
        print("ERROR DEL ID")

def borrar():
    mostrar()
    seleccion = input("Ingrese ID del juego a eliminar: ")
    if seleccion in juegos:
        del juegos[seleccion]
        del precios[seleccion]
        mostrar()
    else:
        print("ERROR DEL ID")

def agregar():
    juego_nuevo = input("Ingrese nombre del juego: ")
    consola = input("Ingrese consola del juego (Xbox, Pc, Playstation, Switch): ")
    if consola.lower() not in ["xbox", "pc", "playstation", "switch"]:
        print("ERROR CONSOLA INEXISTENTE")
    else:
        fecha = input("Ingrese fecha del juego: ")
        if len(fecha) == 4 and fecha.isdigit():
            id_nuevo = input("Ingrese ID con una letra en mayuscula y tres numeros: ")
            if len(id_nuevo) == 4 and id_nuevo[:1].isalpha() and id_nuevo[:1].isupper() and id_nuevo[1:].isdigit() and id_nuevo not in juegos:
                print("ID correcto")
                stock = int(input("Ingrese stock del juego: "))
                precio_nuevo = int(input("Ingrese precio del juego: "))
                juegos[id_nuevo] = [juego_nuevo, consola, fecha]
                precios[id_nuevo] = [stock, precio_nuevo]
                mostrar()
            else:
                print("ERROR DE ID")
        else:
            print("ERROR DE FECHA")

while True:
    op = int(input('''
Ingrese opcion:
                   1. Mostrar juegos
                   2. Juego mas caro
                   3. Actualizar precio
                   4. Borrar juego
                   5. Agregar juego
                   6. Salir
'''))
    match op:
        case 1:
            mostrar()
        case 2:
            caro()
        case 3:
            actualizar_precio()
        case 4:
            borrar()
        case 5:
            agregar()
        case 6:
            print("Saliendo...")
            break
        case _:
            print("ERROR")