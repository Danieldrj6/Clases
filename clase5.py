# Match

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado de la suma es: {n1 + n2}")


def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado de la resta es: {n1 - n2}")


def multiplicacion():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado de la multiplicacion es: {n1 * n2}")


def division():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado de la division es: {n1 / n2}")


while True:
    op=int(input('''Seleccione su opcion
                1. suma
                2. resta
                3. multiplicacion
                4. division
                5. salir
                '''))
    match op:                       # match: Es como un menu o lista de opciones
        case 1:                     # case: Son para los diferentes casos
            suma()
        case 2:
            resta()
        case 3:
            multiplicacion()
        case 4:
            division()
        case 5:
            print("Saliendo...")
            break                   # break: Es para romper el bucle
        case _:                     # El _ significa el resto de casos
            print("opcion invalida")