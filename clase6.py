# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         if num >= 3:
#             break
#     except Exception:
#         print("No es un numero")

nombre_boleta = ""

def nombre():
    global nombre_boleta
    nombre_boleta = str(input("Ingrese su nombre o usuario: "))

carro=0
items=0
bazooka=0
rifle=0
escopeta=0
pistola=0
sniper=0

def comprar():
    global carro, bazooka, rifle, escopeta, pistola, sniper, items
    while True:
        comprar_productos=int(input('''
        Productos disponibles:
                        1. Bazooka $20000
                        2. Rifle $5000
                        3. Escopeta $3500
                        4. Pistola $1500
                        5. Sniper $10000
                        6. Salir
        (El minimo de compra es de 3 productos)
    '''))
        match comprar_productos:
            case 1:
                print("Agregaste una Bazooka al carrito mi negro")
                carro+=20000
                items+=1
                bazooka+=1
            case 2:
                print("Agregaste un rifle al carrito mi negro")
                carro+=5000
                items+=1
                rifle+=1
            case 3:
                print("Agregaste una escopeta al carrito mi negro")
                carro+=3500
                items+=1
                escopeta+=1
            case 4:
                print("Agregaste una pistola al carrito mi negro")
                carro+=1500
                items+=1
                pistola+=1
            case 5:
                print("Agregaste un sniper al carrito mi negro")
                carro+=10000
                items+=1
                sniper+=1
            case 6:
                    if items >= 3:
                        print(f"Llevas {items} productos y tienes de precio neto: {carro}")
                        break
                    else:
                        print("El minimo de compra es de 3 productos por favor siga agregando al carrito")
            case _:
                print("Error")

def boleta():
    if nombre_boleta:
            print(f'''
            Boleta:
                Hola, {nombre_boleta} esta es tu boleta!
                Tu precio neto es de: {carro}
                Tu precio final con iva es de {carro*1.19}
                Tienes en el carrito estos productos:
                    bazooka: {bazooka}
                    rifle: {rifle}
                    escopeta: {escopeta}
                    pistola: {pistola}
                    sniper: {sniper}
                Con un total de {items} productos
''')
    else:
        print(f'''
        Boleta:
            Tu precio neto es de: {carro}
            Tu precio final con iva es de {carro*1.19}
            Tienes en el carrito estos productos:
                bazooka: {bazooka}
                rifle: {rifle}
                escopeta: {escopeta}
                pistola: {pistola}
                sniper: {sniper}
            Con un total de {items} productos
''')


print("Bienvenido al carrito de supermercado de python")
while True:
    op=int(input('''
        Opciones:
        1. Ingresar nombre
        2. Comprar
        3. Boleta
        4. Salir
    '''))
    match op:
        case 1:
            nombre()
        case 2:
            comprar()
        case 3:
            boleta()
        case 4:
            print("Saliendo...")
            break