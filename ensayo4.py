viajes = {
    'V001': ['Puerto Varas', 'Bus'],
    'V002': ['La Serena', 'Avión'],
    'V003': ['Pucón', 'Bus']
}

# reservas id = [precio por persona, cantidad de reservas]
reservas = {
    'V001': [25000, 20],
    'V002': [75000, 5],
    'V003': [28000, 0]
}

# mostrar viajes
# Viaje más económico
# Agregar reservas
# Cancelar viaje (solo si no tiene reservas)
# Editar medio de transporte y viaje
# Quitar una reserva
# Agregar viaje
# Salir

def mostrar():
    for ids, viaje in viajes.items():
        print(f"Viaje con ID: {ids} hacia {viaje[0]} en {viaje[1]} por tan solo ${reservas[ids][0]}! ya hay {reservas[ids][1]} reservas!")

def precio(ids):
    return reservas[ids][0]

def economico():
    modelo_eco = min(reservas, key=precio)
    print(f"El viaje mas economico es el de {viajes[modelo_eco][0]} en {viajes[modelo_eco][1]} por ${reservas[modelo_eco][0]}")

def agregar_reserva():
    mostrar()
    seleccion = input("Ingrese ID del viaje a reservar: ")
    if seleccion not in viajes:
        print("ERROR DE ID")
    else:
        reservas[seleccion][1] +=1
        print("Reserva realizada!")
        mostrar()

def cancelar():
    for ids, viaje in viajes.items():
        if reservas[ids][1] == 0:
            print(f"Viaje con ID: {ids} hacia {viaje[0]} en {viaje[1]} por ${reservas[ids][0]} hay {reservas[ids][1]} reservas")
    seleccion = input("Ingrese ID de viaje a cancelar: ")
    if seleccion not in viajes:
        print("No hay viajes para cancelar o tu id es invalido...")
    else:
        del viajes[seleccion]
        del reservas[seleccion]
        print("Viaje eliminado por falta de reservas")
        mostrar()

def editar():
    mostrar()
    seleccion = input("Ingrese ID del viaje a modificar: ")
    if seleccion not in viajes:
        print("ERROR DE ID")
    else:
        transporte = input("Ingrese transporte (bus, avion, barco o tren): ")
        if transporte.lower() not in ["bus", "avion", "barco", "tren"]:
            print("Transporte invalido")
        else:
            viaje = input("Ingrese destino del viaje: ")
            precio_nuevo = int(input("Ingrese precio del viaje: "))
            viajes[seleccion] = [viaje, transporte]
            reservas[seleccion][0] = precio_nuevo
            print("Viaje cambiado con exito!")
            mostrar()

def quitar_reserva():
    mostrar()
    seleccion = input("Ingrese ID de la reserva a quitar: ")
    if seleccion not in viajes or reservas[seleccion][1] == 0:
        print("ERROR DE ID O NO HAY RESERVAS A BORRAR")
    else:
        reservas[seleccion][1] -= 1
        print("Reserva cancelada y borrada con exito!")
        mostrar()

def agregar():
    destino = input("Ingrese destino del viaje: ")
    transporte = input("Ingrese transporte (bus, avion, barco o tren): ")
    if transporte.lower() not in ["bus", "avion", "barco", "tren"]:
        print("TRANSPORTE INVALIDO")
    else:
        precio = int(input("Ingrese precio por persona: "))
        ids_nuevo = input("Ingrese ID del viaje (formato: J003): ")
        if len(ids_nuevo) == 4 and ids_nuevo[:1].isalpha() and ids_nuevo[:1].isupper() and ids_nuevo[1:].isdigit() and ids_nuevo not in viajes:
            print("ID correcto!")
            viajes[ids_nuevo] = [destino, transporte]
            reservas[ids_nuevo] = [precio, 0]
            mostrar()
        else:
            print("ERROR DE ID")

while True:
    op = int(input('''
Ingrese opcion:
          1. Mostrar viajes
          2. Viaje mas economico
          3. Agregar reserva
          4. Cancelar viaje sin reservas
          5. Editar medio de transporte, destino y precio
          6. Quitar una reserva
          7. Agregar viaje
          8. Salir
'''))
    match op:
        case 1:
            mostrar()
        case 2:
            economico()
        case 3:
            agregar_reserva()
        case 4:
            cancelar()
        case 5:
            editar()
        case 6:
            quitar_reserva()
        case 7:
            agregar()
        case 8:
            print("Saliendo...")
            break
        case _:
            print("ERROR")