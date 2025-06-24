juegos = {
    1:{"nombre":"super smash bros", "precio":70000, "consola":"switch"},
    2:{"nombre":"sonic colors ultimate", "precio": 35000, "consola":"switch"}
}

def mostrar():
    for ids, juego in juegos.items():
        print(f"ID: {ids}")
        for key, valor in juego.items():
            print(f"{key}: {valor}")

def registrar():
    juego_nuevo = str(input("Ingrese el nombre del juego: "))
    precio_juego = int(input("Ingrese precio del juego: "))
    consola_juego = input("Ingrese consola del juego: ")
    sig_id = max(juegos.keys()) + 1
    juegos[sig_id] = {"nombre":juego_nuevo, "precio":precio_juego, "consola":consola_juego}
    print("--------")
    mostrar()
    print("Juego agregado!")

def actualizar():
    mostrar()
    seleccion = int(input("Ingrese id del juego a actualizar: "))
    juego_nuevo = str(input("Ingrese el nombre del juego: "))
    precio_juego = int(input("Ingrese precio del juego: "))
    consola_juego = input("Ingrese consola del juego: ")
    juegos[seleccion] = {"nombre":juego_nuevo, "precio":precio_juego, "consola":consola_juego}
    print("----------")
    mostrar()
    print("Juego actualizado!")

def borrar():
    mostrar()
    seleccion_borrar = int(input("Ingrese id del juego a borrar: "))
    del juegos[seleccion_borrar]
    print("----------")
    mostrar()
    print("Juego borrado!")

while True:
    op = int(input('''
    Ingrese opcion:
                   1. agregar juego
                   2. borrar juego
                   3. actualizar juego
                   4. mostrar lista de juegos
                   5. salir
'''))
    
    match op:
        case 1:
            registrar()
        case 2:
            borrar()
        case 3:
            actualizar()
        case 4:
            mostrar()
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Error")