
celulares = {
    'C001': ['Samsung', 'S21', 2021, 'Android'],
    'C002': ['Apple', 'iPhone 13', 2021, 'iOS'],
    'C003': ['Xiaomi', 'Note 10', 2022, 'Android']
}
inventario = {
    'C001': [799000, 10],
    'C002': [999000, 5],
    'C003': [499000, 0],
    'C999': [599000, 2]  # No registrado en celulares
}
# menu:
# Ver catálogo de celulares disponibles (solo los con stock > 0)
# Mostrar celular con el celular mas caro
# Editar precio de un modelo
# Registrar un nuevo celular
# Eliminar celular del inventario (solo si no tiene stock)
# Salir

def mostrar():
    for ids, celu in celulares.items():
        if inventario[ids][1] > 0:
            print(f"Celular ID: {ids} {celu[0]} {celu[1]} {celu[3]} con fecha del {celu[2]} y stock: {inventario[ids][1]} con precio c/u de {inventario[ids][0]}")

def precio(ids):
    return inventario[ids][0]

def caro():
    celular_caro = max(inventario, key=precio)
    print(f"El celular mas caro es el: {celulares[celular_caro][0]} {celulares[celular_caro][1]} con precio de ${inventario[celular_caro][0]}")

def editar_precio():
    mostrar()
    seleccion = input("Ingrese ID del precio del celular a editar: ")
    if seleccion not in celulares:
        print("ERROR DE ID")
    else:
        precio_nuevo = int(input("Ingrese precio nuevo: "))
        inventario[seleccion][0] = precio_nuevo
        print("Precio corregido!")
        mostrar()

def registro():
    marca = input("Ingrese marca del telefono: ")
    modelo = input("Ingrese modelo del telefono: ")
    fecha = input("Ingrese fecha del telefono: ")
    if len(fecha) == 4 and fecha.isdigit():
        bios = input("Ingrese sistema operativo o bios: ")
        if bios.lower() not in ["ios", "android", "harmonyos"]:
            print("ERROR DE BIOS")
        else:
            precio = int(input("Ingrese precio del celular a vender: "))
            stock = int(input("Ingrese stock: "))
            ids_nuevo = input("Ingrese ID del telefono (primera letra mayuscula y 3 numeros): ")
            if len(ids_nuevo) == 4 and ids_nuevo[:1].isalpha() and ids_nuevo[:1].isupper() and ids_nuevo[1:].isdigit() and ids_nuevo not in celulares:
                print("ID correcto!")
                celulares[ids_nuevo] = [marca, modelo, fecha, bios]
                inventario[ids_nuevo] = [precio, stock]
                mostrar()
            else:
                print("ERROR DE ID")
    else:
        print("ERROR DE FECHA")

def eliminar():
    for ids, celu in celulares.items():
            print(f"Celular ID: {ids} {celu[0]} {celu[1]} {celu[3]} con fecha del {celu[2]} y stock: {inventario[ids][1]} con precio c/u de {inventario[ids][0]}")
    seleccion = input("Ingrese ID del telefono a eliminar: ")
    if seleccion not in celulares or inventario[seleccion][1] > 0:
        print("ERROR DE ID O AUN TIENE STOCK")
    else:
        del celulares[seleccion]
        del inventario[seleccion]
        print("Celular borrado por falta de stock")
        for ids, celu in celulares.items():
            print(f"Celular ID: {ids} {celu[0]} {celu[1]} {celu[3]} con fecha del {celu[2]} y stock: {inventario[ids][1]} con precio c/u de {inventario[ids][0]}")

while True:
    op = int(input('''
Ingrese opcion:
          1. Mostrar catalogo disponible
          2. Mostrar celular mas caro
          3. Editar precio
          4. Registrar nuevo celular
          5. Eliminar celular
          6. Salir
'''))
    match op:
        case 1:
            mostrar()
        case 2:
            caro()
        case 3:
            editar_precio()
        case 4:
            registro()
        case 5:
            eliminar()
        case 6:
            print("Saliendo...")
            break
        case _:
            print("ERROR")