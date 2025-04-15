print("Bienvenido al hotel de Python!")
dinero=int(input("Escribe el dinero que simulas que tienes: "))
nombre=str(input("Escribe tu nombre: "))
edad=int(input("Escribe tu edad: "))
if edad >= 18:
    print("Hola", nombre, "Eres mayor de edad ya que tienes", edad, "años")
    print("Puedes entrar al hotel")
    print("Hay diferentes habitaciones")
    print("1. Habitacion sencilla por el costo de $1000")
    print("2. Habitacion doble por el costo de $2000")
    print("3. Habitacion suite por el costo de $3000")
    respuesta=int(input("Escribe el numero de la habitacion que deseas: "))
    if respuesta == 1:
        print("Has elegido la habitacion sencilla")
        if dinero >= 1000:
            print("Puedes entrar a la habitacion")
            dinero = dinero - 1000
            print("Tu dinero ahora es de", dinero)
        else:
            print("No tienes suficiente dinero")
    elif respuesta == 2:
        print("Has elegido la habitacion doble")
        if dinero >= 2000:
            print("Puedes entrar a la habitacion")
            dinero = dinero - 2000
            print("Tu dinero ahora es de", dinero)
        else:
            print("No tienes suficiente dinero")
    elif respuesta == 3:
        print("Has elegido la habitacion suite")
        if dinero >= 3000:
            print("Puedes entrar a la habitacion")
            dinero = dinero - 3000
            print("Tu dinero ahora es de", dinero)
        else:
            print("No tienes suficiente dinero")
else:
    print("Eres menor de edad")
    print("No puedes entrar al hotel")