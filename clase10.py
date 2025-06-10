
# Listas y Diccionarios

# El array se usa de la siguiente manera:
# array = [1, 2, 3, 4, 5]
# El array es una lista de elementos que se pueden acceder por su indice

# mi_lista=[1,2,3,4,5,]
# print(mi_lista[2])
# # las listas empiezan del 0 por lo tanto 1 = 0, 2 = 1, 3 = 2 por ello en el print se da el numero 3
# # .insert es para agregar un elemento a la lista
# mi_lista.insert(3, 10)
# print(mi_lista)
# mi_lista.pop(3)
# print(mi_lista)
# mi_lista.reverse()
# mi_lista.sort()

def agregar():
    
    global lista_productos, carrito

    lista_productos = ["bazooka", "sniper", "pistola", "rifle", "granada"]
    carrito = []
    while True:
        ops=int(input("Ingrese su producto a agregar: " \
        "1. bazooka " \
        "2. sniper " \
        "3. pistola " \
        "4. rifle " \
        "5. granada " \
        "6. salir"))
        match ops:
            case 1:
                print("Su ", lista_productos[0], "ha sido agregado al carrito")
                carrito.insert(0, lista_productos[0])
            case 2:
                print("Su ", lista_productos[1], "ha sido agregado al carrito")
                carrito.insert(0,lista_productos[1])
            case 3:
                print("Su ", lista_productos[2], "ha sido agregado al carrito")
                carrito.insert(0,lista_productos[2])
            case 4:
                print("Su ", lista_productos[3], "ha sido agregado al carrito")
                carrito.insert(0,lista_productos[3])
            case 5:
                print("Su ", lista_productos[4], "ha sido agregado al carrito")
                carrito.insert(0,lista_productos[4])
            case 6:
                 break

def mostrar():
    print("Usted tiene estos productos en el carrito: ", carrito)

while True:
    op=int(input('''
Ingrese opcion:
        1. Agregar un producto
        2. Eliminar un producto listado
        3. Mostrar productos
        4. Salir
'''))
    match op:
        case 1:
            agregar()
        case 2:
            print(1)
        case 3:
            mostrar()
        case 4:
            break
