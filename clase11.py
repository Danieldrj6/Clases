# nombre = []
# apellido = []
# contador = 0

# while True:
#     op=int(input('''
#         1. Ingresar nombre y apellido
#         2. Mostrar nombres y apellidos
#         3. Buscar nombre
#         4. Salir
# '''))
#     match op:
#         case 1:
#             nombre.append(input("Ingrese su nombre: "))
#             apellido.append(input("Ingrese su apellido: "))
#         case 2:
#             for nombres in nombre:
#                 print(nombre[contador], apellido[contador])
#                 contador += 1
#         case 3:
#             nom=str(input("Ingrese nombre a buscar: "))
#             if nom in nombre:
#                 print(f"El nombre {nom} esta registrado")
#             else:
#                 print("No existe")
#         case 4:
#             break
#         case _:
#             print("Error")

# Carrito de compras 3.0

productos = []
precios = []
carrito = []

def ingresar():
    while True:
        op1=int(input('''
        Seleccione opcion:
                      1. agregar producto
                      2. salir
'''))
        match op1:
            case 1:
                productos.append(str(input("Ingrese nombre del producto: ")))
                precios.append(int(input("Ingrese precio: ")))
                print(f"Estos son los productos y precios en lista: ")
                for producto in productos:
                    p = 0
                    print(productos[p], precios[p])
                    p += 1

        
while True:
    op = int(input('''
        Ingrese opcion:
                    1. Ingresar productos
                    2. Comprar
                    3. Crear boleta
                    4. Salir
'''))
    match op:
        case 1:
            ingresar()
        case 1:
            print("")
        case 3:
            print("S")
        case 4:
            break

                