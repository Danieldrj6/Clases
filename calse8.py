import time as tm

print("Bienvenido al restaurante de sushi de python!")

def menu():
    global pkr, otr, pvr, aer, rolls, cant_pkr, cant_otr, cant_pvr, cant_aer, descuento, subtotal, total, codigo_correcto
    codigo_correcto = "soyotaku"
    pkr = 0
    otr = 0
    pvr = 0
    aer = 0
    rolls = 0
    cant_pkr = 0
    cant_otr = 0
    cant_pvr = 0
    cant_aer = 0
    total = 0
    subtotal = 0

    while True:
        ops = int(input('''Ingrese los sushis que desea llevar: 
                  1. Pikachu Roll $4500
                  2. Otaku Roll $5000
                  3. Pulpo Venenoso Roll $5200
                  4. Anguila Electrica Roll $4800 
                  5. Salir
                  '''))
        match ops:
            case 1:
                print("Agregado en el carrito tu Pikachu Roll!")
                pkr += 4500
                rolls += 1
                cant_pkr += 1
                subtotal = pkr + otr + pvr + aer
                total = subtotal
                print(f'''
Esta es tu boleta actualmente:
                    ********************************
                    TOTAL PRODUCTOS: {rolls}
                    ********************************
                    Pikachu Roll: {cant_pkr}
                    Otaku Roll: {cant_otr}
                    Pulpo Venenoso Roll: {cant_pvr}
                    Anguila Electrica Roll: {cant_aer}
                    ********************************
                    Subtotal por pagar: ${subtotal}
                    TOTAL: ${total}
                    ********************************''')
            case 2:
                print("Agregado en el carrito tu Otaku Roll!")
                otr += 5000
                rolls += 1
                cant_otr += 1
                subtotal = pkr + otr + pvr + aer
                total = subtotal
                print(f'''
Esta es tu boleta actualmente:
                    ********************************
                    TOTAL PRODUCTOS: {rolls}
                    ********************************
                    Pikachu Roll: {cant_pkr}
                    Otaku Roll: {cant_otr}
                    Pulpo Venenoso Roll: {cant_pvr}
                    Anguila Electrica Roll: {cant_aer}
                    ********************************
                    Subtotal por pagar: ${subtotal}
                    TOTAL: ${total}
                    ********************************''')
            case 3:
                print("Agregado en el carrito tu Pulpo Venenoso Roll!")
                pvr += 5200
                rolls += 1
                cant_pvr += 1
                subtotal = pkr + otr + pvr + aer
                total = subtotal
                print(f'''
Esta es tu boleta actualmente:
                    ********************************
                    TOTAL PRODUCTOS: {rolls}
                    ********************************
                    Pikachu Roll: {cant_pkr}
                    Otaku Roll: {cant_otr}
                    Pulpo Venenoso Roll: {cant_pvr}
                    Anguila Electrica Roll: {cant_aer}
                    ********************************
                    Subtotal por pagar: ${subtotal}
                    TOTAL: ${total}
                    ********************************''')
            case 4:
                print("Agregado en el carrito tu Anguila Electrica Roll!")
                aer += 4800
                rolls += 1
                cant_aer += 1
                subtotal = pkr + otr + pvr + aer
                total = subtotal
                print(f'''
Esta es tu boleta actualmente:
                    ********************************
                    TOTAL PRODUCTOS: {rolls}
                    ********************************
                    Pikachu Roll: {cant_pkr}
                    Otaku Roll: {cant_otr}
                    Pulpo Venenoso Roll: {cant_pvr}
                    Anguila Electrica Roll: {cant_aer}
                    ********************************
                    Subtotal por pagar: ${subtotal}
                    TOTAL: ${total}
                    ********************************''')
            case 5:
                break
            case _:
                print("Error")

def pagar():
    print(f'''
Esta es tu boleta:
                    ********************************
                    TOTAL PRODUCTOS: {rolls}
                    ********************************
                    Pikachu Roll: {cant_pkr}
                    Otaku Roll: {cant_otr}
                    Pulpo Venenoso Roll: {cant_pvr}
                    Anguila Electrica Roll: {cant_aer}
                    ********************************
                    Subtotal por pagar: ${subtotal}
                    TOTAL: ${total}
                    ********************************''')
    desc_sn=str(input("Desea agregar un codigo de descuento?: s/n: "))
    if desc_sn == "s":
        codigo=str(input("Ingrese su codigo: "))
        if codigo==codigo_correcto:
            descuento = subtotal * 0.10
            total = subtotal - descuento
            print(f'''
                        ********************************
                        TOTAL PRODUCTOS: {rolls}
                        ********************************
                        Pikachu Roll: {cant_pkr}
                        Otaku Roll: {cant_otr}
                        Pulpo Venenoso Roll: {cant_pvr}
                        Anguila Electrica Roll: {cant_aer}
                        ********************************
                        Subtotal por pagar: ${subtotal}
                        Descuento por codigo: ${descuento}
                        TOTAL: ${total}
                        ********************************''')
            print("Gracias por venir")
        else:
            print("Error")
    elif desc_sn == "n":
        print(f'''
                        ********************************
                        TOTAL PRODUCTOS: {rolls}
                        ********************************
                        Pikachu Roll: {cant_pkr}
                        Otaku Roll: {cant_otr}
                        Pulpo Venenoso Roll: {cant_pvr}
                        Anguila Electrica Roll: {cant_aer}
                        ********************************
                        Subtotal por pagar: ${subtotal}
                        TOTAL: ${total}
                        ********************************''')
        print("Gracias por venir!")
    else:
        print("Error")

while True:
    op=int(input('''
Ingrese una opcion:
             1. Menu
             2. Pagar
             3. Salir
'''))
    match op:
        case 1:
            menu()
        case 2:
            pagar()
        case 3:
            print("Saliendo...")
            tm.sleep(2.5)
            print("Gracias por su visita!")
            break
        case _:
            print("Error")
