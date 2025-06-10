nombre = []
apellido = []
contador = 0

while True:
    op=int(input('''
        1. Ingresar nombre y apellido
        2. Mostrar nombres y apellidos
        3. Buscar nombre
        4. Salir
'''))
    match op:
        case 1:
            nombre.append(input("Ingrese su nombre: "))
            apellido.append(input("Ingrese su apellido: "))
        case 2:
            for nombres in nombre:
                print(nombre[contador], apellido[contador])
                contador += 1
        case 3:
            nom=str(input("Ingrese nombre a buscar: "))
            if nom in nombre:
                print(f"El nombre {nom} esta registrado")
            else:
                print("No existe")
        case 4:
            break
        case _:
            print("Error")
                