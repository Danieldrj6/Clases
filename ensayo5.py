
# id-> producto, tipo, marca, stock
productos = {
    'P001': ['Notebook', 'Computación', 'Lenovo', 5],
    'P002': ['Smartphone', 'Telefonía', 'Samsung', 10],
    'P003': ['Smartwatch', 'Wearables', 'Apple', 0],
}
# id -> precio, descuento en porcentaje
precios = {
    'P001': [599000, 10],
    'P002': [349000, 0],
    'P003': [279000, 15],
}
# id -> ventas totales
ventas = {
    'P001': 1,
    'P002': 0,
    'P003': 0
}

# 1. Ver productos con stock y precio final
# 2. Vender producto (actualiza stock y ventas)
# 3. Producto más vendido
# 4. Cambiar precio o descuento
# 5. Agregar nuevo producto
# 6. Eliminar producto (si stock y ventas son 0)
# 7. Mostrar ganancias totales por producto
# 8. Salir

def mostrar():
    for ids, producto in productos.items():
        print(f"ID: {ids}/ {producto[0]} con stock de: {producto[3]} a ${precios[ids][0]} c/a")
        print(f"Ventas del producto {producto[0]}: {ventas[ids]}")

def vender():
    mostrar()
    venta = input("Ingrese ID del producto a vender: ")
    if venta not in productos or productos[venta][3] == 0:
        print("ERROR DE ID O NO HAY STOCK")
    else:
        productos[venta][3] -= 1
        ventas[venta] += 1
        mostrar()

def max_ventas(ids):
    return ventas[ids]

def mas_vendido():
    vendido = max(ventas, key=max_ventas)
    print(f"El producto mas vendido es: {productos[vendido][0]} con una cantidad de ventas de: {ventas[vendido]}")

def editar():
    mostrar()
    seleccion = input("Ingrese ID del producto a editar: ")
    if seleccion not in productos:
        print("ERROR DE ID")
    else:
        precio_nuevo = int(input("Ingrese precio: "))
        descuento = int(input("Ingrese descuento total: "))
        precios[seleccion] = [precio_nuevo, descuento]
        mostrar()

def agregar():
    producto = input("Ingrese nombre del producto: ")
    tipo = input("Ingrese tipo de producto: ")
    marca = input("Ingrese marca de producto: ")
    stock = int(input("Ingrese stock inicial: "))
    precio = int(input("Ingrese precio del producto: "))
    desc = int(input("Ingrese descuento: "))
    ids_nuevo = input("Ingrese ID (Formato: J009): ")
    if len(ids_nuevo) == 4 and ids_nuevo[:1].isalpha() and ids_nuevo[:1].isupper() and ids_nuevo[1:].isdigit and ids_nuevo not in productos:
        productos[ids_nuevo] = [producto, tipo, marca, stock]
        precios[ids_nuevo] = [precio, desc]
        ventas[ids_nuevo] = 0
    else:
        print("ERROR DE ID")

def eliminar():
    for ids, producto in productos.items():
        if productos[ids][3] == 0 and ventas[ids] == 0:
            print(f"ID: {ids}/ {producto[0]} con stock de: {producto[3]} a ${precios[ids][0]} c/a")
            print(f"Ventas del producto {producto[0]}: {ventas[ids]}")
    seleccion = input("Ingrese ID del producto a eliminar: ")
    if seleccion not in productos:
        print("ERROR")
    else:
        del productos[seleccion]
        del precios[seleccion]
        del ventas[seleccion]
        print("Producto borrado!")
        mostrar()

while True:
    op = int(input('''
Ingrese opcion:
          1. Mostrar catalogo
          2. Vender producto
          3. Producto mas vendido
          4. Cambiar precio
          5. Agregar producto
          6. Eliminar producto
          7. Salir
'''))
    match op:
        case 1:
            mostrar()
        case 2:
            vender()
        case 3:
            mas_vendido()
        case 4:
            editar()
        case 5:
            agregar()
        case 6:
            eliminar()
        case 7:
            print("Saliendo")
            break
        case _:
            print("ERROR")