# productos = [
#     {"nombre":"lapiz", "precio":400},
#     {"nombre":"goma", "precio":200},
#     {"nombre":"estuche", "precio":1000}
# ]
# c=0
# for producto in productos:
#     print(f"El producto {productos[0+c]["nombre"]} tiene el precio de {productos[0+c]["precio"]}")
#     c+=1

lista = [
    {"nombre":"lapiz", "precio": 200},
    {"nombre":"estuche", "precio":1000},
    {"nombre":"M9 doppler phase 2", "precio":2500000},
    {"nombre":"Anais (la mamita de sami)", "precio":1000000000000000}
]

def agregar():
    nombre = input("Agregue el nombre del producto: ")
    precio = int(input("Agregue el precio: "))
    producto = {"nombre": nombre, "precio": precio}
    lista.append(producto)

def borrar():
    c=0
    num_list=0
    print("Hay estos productos:")
    for producto in lista:
         print(f"El producto {num_list+1}. {lista[0+c]["nombre"]} y tiene el precio de {lista[0+c]["precio"]}")
         c+=1
         num_list+=1
    borrar_pro=int(input("Ingrese numero de producto a borrar: "))
    del lista[borrar_pro-1]

def actualizar():
    c=0
    num_list=0
    print("Hay estos productos:")
    for producto in lista:
         print(f"El producto {num_list+1}. {lista[0+c]["nombre"]} y tiene el precio de {lista[0+c]["precio"]}")
         c+=1
         num_list+=1
    actualizar_pro=int(input("seleccione el producto a actualizar: "))
    lista[actualizar_pro-1]["precio"]=int(input("Ingrese el nuevo precio: "))

def mostrar():
    c=0
    for producto in lista:
        print(f"El producto {lista[0+c]["nombre"]} y tiene el precio de {lista[0+c]["precio"]}")
        c+=1

while True:
    op=int(input('''
    Ingrese una opcion:
                 1. Agregar un producto
                 2. Borrar un producto
                 3. Actualizar producto
                 4. Mostrar productos
                 5. Salir
'''))
    match op:
        case 1:
            agregar()
        case 2:
            borrar()
        case 3:
            actualizar()
        case 4:
            mostrar()
        case 5:
            print("saliendo...")
            break
        case _:
            print("Error")


