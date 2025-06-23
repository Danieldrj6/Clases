personas = {
    1:{"nombre":"daniel", "telefono": 932445769, "rut":216809890},
    2:{"nombre":"juliana", "telefono": 949537833, "rut":230420556}
}

'''
Programa que registre una nueva persona, borre personas, actualice personas y muestre personas y su respectiva info
'''

def registrar():
    persona=str(input("Ingrese nombre: "))
    telefono=int(input("Ingrese su numero de telefono: "))
    if len(str(telefono)) != 9:
        print("ERROR")
        return
    rut=int(input("Ingrese su rut sin puntos o guion: "))
    sig_id=max(personas.keys()) + 1
    personas[sig_id]={
        "nombre":persona,
        "telefono":int(telefono),
        "rut":rut
    }
    print("Usuario agregado")

def borrar():
    for ids, datos in personas.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    seleccion=int(input("Ingrese id a borrar: "))
    del personas[seleccion]

def actualizar():
    for ids, datos in personas.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    seleccion2=int(input("Ingrese id a actualizar: "))
    persona=str(input("Ingrese nombre: "))
    telefono=input("Ingrese su numero de telefono: ")
    if not telefono.isdigit() or len(telefono) != 9:
        print("ERROR")
        return
    rut=int(input("Ingrese su rut sin puntos o guion: "))
    personas[seleccion2]={"nombre":persona, "telefono": telefono, "rut":rut}

def mostrar():
    for ids, datos in personas.items():
        print(f"Id: {ids}")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

while True:
    op=int(input('''Ingrese opcion: 
                1. agregar persona
                2. borrar persona
                3. actualizar persona
                4. mostrar datos de personas
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
            print("ERROR")