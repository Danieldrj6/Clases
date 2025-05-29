import time as tm

while True:
    op=int(input('''
    Seleccione su pañol favorito:
                1. pañol supremo
                2. pañol caca
                3. pañol gay
                4. salir
'''))
    match op:
        case 1:
            for i in range(1,50):
                print("Genial eres el mejor pañol!")
                tm.sleep(0.5)
        case 2:
            for i in range(1,50):
                print("no jodas amigo porque ese pañol?")
                tm.sleep(0.5)
        case 3:
            for i in range(1,50):
                print("Rawr pero que pañol")
                tm.sleep(0.5)
            break
        case 4:
            print("Mish")
            break
        case _:
            print("eso es un pañol?")

