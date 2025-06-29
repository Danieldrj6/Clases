
entradas = [
    {"nombre":"dani","tipo":"G", "codigo":"Pipos1"},
    {"nombre":"jose","tipo":"G", "codigo":"Pipos2"}
]

def validar_nombre():
    for entrada in entradas:
        if entrada["nombre"] == nombre:
            return False
    return True

def validar_tipo():
    return tipo in ["G", "V"]

def validar_codigo():
    if len(codigo) < 6:
        return False
    if not any(c.isupper() for c in codigo):
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    if " " in codigo:
        return False
    return True

def registro():
    global nombre, tipo, codigo
    nombre = input("Ingrese nombre: ")
    while not validar_nombre():
        print("Nombre repetido")
        nombre = input("Ingrese nombre: ")
    tipo = input("Ingrese tipo de entrada G = general, V = Vip: ")
    while not validar_tipo():
        print("ERROR")
        tipo = input("Ingrese tipo de entrada G = general, V = Vip: ")
    codigo = input("Ingrese codigo de 6 caracteres, 1 mayuscula y 1 numero: ")
    while not validar_codigo():
        print("Error en el codigo")
        codigo = input("Ingrese codigo de 6 caracteres, 1 mayuscula y 1 numero: ")
    entradas.append({"nombre":nombre, "tipo":tipo, "codigo":codigo})

def buscar():
    while True:
        buscador = input("Ingrese nombre a buscar: ")
        encontrado = False
        for entrada in entradas:
            if entrada["nombre"] == buscador:
                print(f"Tipo de entrada: {entrada["tipo"]}, codigo: {entrada["codigo"]}")
                encontrado = True
                break
        if not encontrado:
            print("Nombre no encontrado")
            break

# def borrar():
#     borra = int(input("Ingrese nombre a cancelar: "))
#     if borra is not validar_nombre():
#         print("Error")
#         borra = int(input("Ingrese nombre a cancelar: "))
#     del entradas(borra)

while True:
    op = int(input('''
Ingrese opcion:
          1. Comprar
          2. Consultar
          3. Borrar
          4. Salir
'''))
    match op:
        case 1:
            registro()
        case 2:
            buscar()
        case 3:
            print("")
        case 4:
            print("Saliendo...")
        case _:
            print("Error")
