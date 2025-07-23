
# Socios rut -> nombre, edad, plan, actividad
socios = {
    '12.345.678-9': ['Carlos Pérez', 30, 'mensual', 'activo'],
    '98.765.432-1': ['Ana Gómez', 25, 'trimestral', 'activo'],
    '11.111.111-1': ['Luis Soto', 35, 'anual', 'inactivo']
}
# Pagos rut -> pagos realizados, deuda
pagos = {
    '12.345.678-9': [3, 0],
    '98.765.432-1': [1, 50000],
    '11.111.111-1': [2, 0]
}
# 1. Mostrar socios activos
# 2. Ver socios con deuda
# 3. Registrar nuevo socio
# 4. Registrar pago (resta deuda)
# 5. Cambiar estado del socio (activo/inactivo)
# 6. Ver socio con más pagos realizados
# 7. Eliminar socio (solo si no tiene deuda)
# 8. Registrar deuda
# 9. Salir

def mostrar():
    for ruts, gente in socios.items():
        if socios[ruts][3] == 'activo':
            print(f"Socio de rut: {ruts}, Nombre: {gente[0]} con edad de: {gente[1]}, Plan: {gente[2]}, actualmente: {gente[3]}")
        else:
            print(f"No activo actualmente: Socio de rut: {ruts}, Nombre: {gente[0]} con edad de: {gente[1]}, Plan: {gente[2]}")

def deudas():
    for ruts, gente in socios.items():
        if pagos[ruts][1] > 0:
            print(f"La deuda del socio: {gente[0]} con rut: {ruts} tiene una deuda de: {pagos[ruts][1]} pero ha pagado anteriormente {pagos[ruts][0]} veces")
        else:
            print(f"La persona con nombre: {gente[0]} con rut: {ruts} tiene {pagos[ruts][0]} pagos realizados")

def registrar():
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    plan = input("Ingrese plan: ")
    if plan not in ["mensual", "diario", "trimestral", "semestral", "anual"]:
        print("PLAN INVALIDO")
    else:
        rut = input("Ingrese rut: ")
        socios[rut] = [nombre, edad, plan, 'activo']
        pagos[rut] = [1, 0]
        print("Registro realizado!")
        mostrar()

def pago():
    for ruts, gente in socios.items():
        if pagos[ruts][1] > 0:
            print(f"La deuda del socio: {gente[0]} con rut: {ruts} tiene una deuda de: {pagos[ruts][1]} pero ha pagado anteriormente {pagos[ruts][0]} veces")
    seleccion = input("Ingrese rut de la persona a registrar pago: ")
    if seleccion not in socios:
        print("ERROR")
    else:
        pago = int(input("Ingrese cantidad a pagar: "))
        if pago > pagos[seleccion][1]:
            print("ERROR MONTO EXCEDIDO")
        else:
            pagos[seleccion][1] -= pago
            pagos[seleccion][0] += 1
            deudas()
            mostrar()

def actividad():
    mostrar()
    seleccion = input("Ingrese rut de la persona a cambiar actividad: ")
    if seleccion not in socios:
        print("ERROR")
    else:
        actividad = int(input("Ingrese 1 para activar o 2 para deshabilitar: "))
        while actividad not in [1, 2]:
            print("ERROR")
            actividad = int(input("Ingrese 1 para activar o 2 para deshabilitar: "))
        if actividad == 1:
            socios[seleccion][3] = 'activo'
            print("Activado correctamente")
            mostrar()
        else:
            actividad[seleccion][3] = 'inactivo'
            print("Se ha desactivado correctamente")
            mostrar()

def mas(ruts):
    return pagos[ruts][0]

def mas_pagos():
    mas_pagados = max(pagos, key=mas)
    print(f"El usuario con mas pagos registrados es: {socios[mas_pagados][0]} con rut: {mas_pagados} con {pagos[mas_pagados][0]} pagos realizados!")

def eliminar():
    mostrar()
    

    
    
