print("Simulacion de tarjeta de credito")
deuda=100000
pagado=0

def pago():
    print(f"Usted tiene de deuda: {deuda}")
    while True:
        try:
            pagado=int(input("Ingresar monto: "))
            if pagado<=deuda:
                print(f"Usted tiene actualmente de deuda: {deuda}")
                break
        except Exception:
            print("Error en el monto")
    
def simulacion():
    print("Simulación de compras no implementada aún.")

while True:
    op = int(input('''
Ingrese numero para acceder a las opciones:
             1. Pago de tarjeta de credito
             2. Simulacion de compras
             3. Salir
'''))
    match op:
        case 1:
            pago()
        case 2:
            simulacion()
        case 3:
            break

