personas = {
    1: {"nombre": "Juliana",
        "telefono": 123456789,
        "estado civil": "casado",
        "ciudadano": True
        },
    2: {"nombre": "Daniel",
        "telefono": 932445768,
        "estado civil": "casado",
        "ciudadano": True
        }
}

def crear():
    persona=str(input("Ingrese nombre: "))
    telefono = input("Ingrese numero de telefono: ")
    if not telefono.isdigit() or len(telefono) != 9:
        print("El número de teléfono debe tener 9 dígitos.")
        return
    estado_civil = input("Ingrese estado civil (casado/soltero): ").lower()
    if estado_civil not in ("casado", "soltero"):
        print("Error en la respuesta")
        return
    ciudadano = input("El usuario es ciudadano? (s/n): ").lower()
    if ciudadano in ("s", "si"):
        ciudadano = True
    elif ciudadano in ("n", "no"):
        ciudadano = False
    else:
        print("Error")
        return
    sig_id = max(personas.keys(), default=0) + 1
    personas[sig_id] = {
        "nombre": persona,
        "telefono": int(telefono),
        "estado civil": estado_civil,
        "ciudadano": ciudadano
    }
    print("Usuario agregado correctamente.")

def crear_usuario():
    persona = input("Ingrese nombre: ").lower()
    for datos in personas.values():
        if datos["nombre"].lower() == persona:
            print("Este usuario ya existe en el registro")
            return
    telefono = input("Ingrese numero de telefono: ")
    if not telefono.isdigit() or len(telefono) != 9:
        print("El número de teléfono debe tener 9 dígitos.")
        return
    estado_civil = input("Ingrese estado civil (casado/soltero): ").lower()
    if estado_civil not in ("casado", "soltero"):
        print("Error en la respuesta")
        return
    ciudadano = input("El usuario es ciudadano? (s/n): ").lower()
    if ciudadano in ("s", "si"):
        ciudadano = True
    elif ciudadano in ("n", "no"):
        ciudadano = False
    else:
        print("Error")
        return
    sig_id = max(personas.keys(), default=0) + 1
    personas[sig_id] = {
        "nombre": persona,
        "telefono": int(telefono),
        "estado civil": estado_civil,
        "ciudadano": ciudadano
    }
    print("Usuario agregado correctamente.")

def actualizar():
    for ids, datos in personas.items():
        print(f"ID: {ids}")
        for clave, valor in datos.items():
            print(f"  {clave}: {valor}")
    seleccion=int(input("Ingrese id a actualizar: "))
    if seleccion != ids:
        print("Error")
    else:
        personas[seleccion]=crear()

def mostrar():
    for ids, datos in personas.items():
        print(f"ID: {ids}")
        for clave, valor in datos.items():
            print(f"  {clave}: {valor}")

while True:
    op=int(input('''
    Ingrese opcion:
                1. Agregar info persona
                2. Actualizar info persona
                3. Borrar persona
                4. Mostrar personas
                5. Salir
    '''))
    match op:
        case 1:
            crear_usuario()
        case 2:
            actualizar()
        case 3:
            print("")
        case 4:
            mostrar()
        case 5:
            print("Saliendo...")
            break