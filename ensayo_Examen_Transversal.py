
autos = {
    'ABC123': ['Toyota', 2020, 'Gasolina', '1.6L'],
    'DEF456': ['Chevrolet', 2019, 'Diesel', '2.0L'],
    'GHI789': ['Hyundai', 2021, 'Eléctrico', '0.0L'],
    'JKL321': ['Mazda', 2022, 'Gasolina', '2.5L']
}
# stock tiene el medelo del auto para hacer el cruce entre diccionarios
# cada par de datos tiene el modelo y la cantidad de stock y el precio del mismo,
stock = {
    'ABC123': [14, 12500000],
    'DEF456': [0, 10400000],
    'GHI789': [4, 17900000],
    'JKL321': [6, 15500000],
    'ZZZ000': [2, 8900000]  # Este auto no existe en Autos
}

'''
dado los diccionarios anteriores cerar un programa con sl sigueinte menu
1.- Mostrar stock de cada uno 
2.- Buscar precio mas alto 
3.- Actualizar stock 
4.- Borrar un modelo ( considerar borarr el stock tb)
5.- Actualizar datos vehiculo
6.- Salir
'''

def mostrar_stock():
    for ids, cantidad in stock.items():
            if ids in autos:
                auto=autos[ids]
                stocker=cantidad[0]
                marca=auto[0]
                fecha=auto[1]
                combustible=auto[2]
                litros=auto[3]
                print(f'''ID: {ids},  Auto marca: {marca}, fecha: {fecha}, tipo de combustible: {combustible} con espacio de: {litros}
    stock disponible: {stocker}''')

def obtener_precio(ids):
    return stock[ids][1]

def precio_alto():
    modelo_caro = max(stock, key=obtener_precio)
    print(f'''El auto mas caro es el {autos[modelo_caro][0]} con precio de: ${stock[modelo_caro][1]}''')

def actualizar_stock():
    mostrar_stock()
    seleccion = input("Ingrese id de auto a cambiar stock: ")
    if seleccion in stock:
        stock_nuevo = int(input("Ingresar numero total de stock: "))
        stock[seleccion][0] = stock_nuevo
        mostrar_stock()
    else:
        print("Error de id")

def borrar():
    mostrar_stock()
    seleccion = input("Ingrese id del auto a borrar: ")
    if seleccion in autos and stock:
        del autos[seleccion]
        del stock[seleccion]
        mostrar_stock()
    else:
        print("Id no encontrado")

def actualizar_autos():
    mostrar_stock()
    seleccion = input("Ingrese id del auto a actualizar: ")
    if seleccion in autos:
        marca = input("Ingrese marca del auto: ")
        fecha = int(input("Ingrese fecha: "))
        combustible = input("Ingrese tipo de combustible: ")
        capacidad = float(input("Ingrese capacidad de combustible: "))
        autos[seleccion] = [marca, fecha, combustible, capacidad]
        mostrar_stock()
    else:
        print("Error de id")

while True:
    op = int(input('''
Ingrese opcion:
          1. Mostrar info
          2. Precio mas alto
          3. Actualizar stock
          4. Borrar info
          5. Actualizar auto
          6. Salir
'''))
    match op:
        case 1:
            mostrar_stock()
        case 2:
            precio_alto()
        case 3:
            actualizar_stock()
        case 4:
            borrar()
        case 5:
            actualizar_autos()
        case 6:
            print("Saliendo...")
            break
        case _:
            print("ERROR")