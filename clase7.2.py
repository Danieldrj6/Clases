import time as tm

dinero=100000
full=0
standard=0
basico=0
auto=0
full_ganado=0
standard_ganado=0
basico_ganado=0

print("Bienvenido al lavado de autos de python!")

def lavado():
    global full, dinero, full_ganado, standard, standard_ganado, basico, basico_ganado, auto
    while True:
        ops=int(input('''
                Seleccione una opcion de lavado:
    1. full $15000
    2. standard $10000
    3. basico $7000
    4. salir
'''))
        match ops:
            case 1:
                print("lavando completamente el auto esto puede demorar...")
                tm.sleep(5.0)
                print("Completado!")
                print("Descontando monto del servicio de su dinero...")
                tm.sleep(1.0)
                print("Gracias por su visita!")
                full+=1
                dinero-=15000
                full_ganado+=15000
                auto+=1
            case 2:
                print("Lavando por fuera su vehiculo con productos de alta calidad, esto puede demorar...")
                tm.sleep(3.5)
                print("Completado!")
                print("Descontando monto del servicio de su dinero...")
                tm.sleep(1.0)
                print("Gracias por su visita!")
                standard+=1
                dinero-=10000
                standard_ganado+=10000
                auto+=1
            case 3:
                print("Lavando su vehiculo con agua y shampoo por favor espere esto puede demorar un poco...")
                tm.sleep(2.0)
                print("Completado!")
                print("Descontando monto del servicio de su dinero...")
                tm.sleep(1.0)
                print("Gracias por su visita!")
                basico+=1
                dinero-=7000
                basico_ganado+=7000
                auto+=1
            case 4:
                break
            case _:
                print("Error")

def ventas():
    print(f'''
    La empresa de lavado de vehiculos tiene este resumen actualmente:
        Lavados full completados: {full} ${full_ganado}
        Lavados standard completados: {standard} ${standard_ganado}
        Lavados basicos completados: {basico} ${basico_ganado}
        Autos que entraron: {auto}
        Total recaudado: ${full_ganado+standard_ganado+basico_ganado}
''')

while True:
    op=int(input('''
    1. menu de lavado
    2. ver ventas diarias
    3. salir
'''))
    match op:
        case 1:
            lavado()
        case 2:
            ventas()
        case 3:
            print("Saliendo")
            break
        case _:
            ("Error")