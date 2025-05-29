
usuario1=""
usuario2=""
usuario3=""

password1=""
password2=""
password3=""

correo=""

def iniciado():
    while True:
        opciones=int(input('''
Ingrese la opcion que desea realizar: 
                           1. realizar llamada
                           2. enviar email
                           3. cerrar sesion
'''))
        match opciones:
            case 1:
                numero=int(input("Ingrese el numero: "))
                if str(numero).startswith('9') and len(str(numero)) == 9:
                    print("Llamando...")
                    print("Llamada exitosa")
                    break
                else:
                    print("El numero debe comenzar con 9 y tener 9 digitos")
            case 2:
                correo=input("Ingrese email: ")
                if "@" in correo:
                    mensaje=input("Ingrese el mensaje a enviar: ")
                    print("Mensaje enviado")
                    break
                else:
                    print("Error no es un correo valido")
            case 3:
                print("Cerrando sesion...")
                break
            case _:
                print("Opcion invalida")


def inicio():
    global usuario1, usuario2, usuario3, password1, password2, password3
    if usuario1 != "" or usuario2 != "" or usuario3 != "":
        usuario = input("Ingrese su usuario: ")
        if usuario == usuario1:
            passw = input("Ingrese su clave: ")
            if passw == password1:
                iniciado()
            else:
                print("Clave incorrecta")
        elif usuario == usuario2:
            passw = input("Ingrese su clave: ")
            if passw == password2:
                iniciado()
            else:
                print("Clave incorrecta")
        elif usuario == usuario3:
            passw = input("Ingrese su clave: ")
            if passw == password3:
                iniciado()
            else:
                print("Clave incorrecta")
        else:
            print("Error: no se reconoce ese usuario en el registro")
    else:
        print("No hay usuarios registrados. Por favor registre un usuario primero.")

def registro():
    global usuario1, usuario2, usuario3, password1, password2, password3
    while True:
        ops = int(input("Ingrese el espacio que quiere usar para su registro: 1, 2, 3 (4 para salir): "))
        match ops:
            case 1:
                if usuario1 != "":
                    print("Ya hay un registro en el primer usuario")
                else:
                    usuario = input("Ingrese su nuevo usuario con solo letras: ")
                    clave = input("Ingrese su nueva clave con solo letras: ")
                    if usuario.isalpha() and clave.isalpha():
                        usuario1 = usuario
                        password1 = clave
                        print("Usuario registrado exitosamente en el primer espacio.")
                    else:
                        print("Solo letras por favor, vuelva a intentar.")
                break
            case 2:
                if usuario2 != "":
                    print("Ya hay un registro en el segundo usuario")
                else:
                    usuario = input("Ingrese su nuevo usuario con solo letras: ")
                    clave = input("Ingrese su nueva clave con solo letras: ")
                    if usuario.isalpha() and clave.isalpha():
                        usuario2 = usuario
                        password2 = clave
                        print("Usuario registrado exitosamente en el segundo espacio.")
                    else:
                        print("Solo letras por favor, vuelva a intentar.")
                break
            case 3:
                if usuario3 != "":
                    print("Ya hay un registro en el tercer usuario")
                else:
                    usuario = input("Ingrese su nuevo usuario con solo letras: ")
                    clave = input("Ingrese su nueva clave con solo letras: ")
                    if usuario.isalpha() and clave.isalpha():
                        usuario3 = usuario
                        password3 = clave
                        print("Usuario registrado exitosamente en el tercer espacio.")
                    else:
                        print("Solo letras por favor, vuelva a intentar.")
                break
            case 4:
                break
            case _:
                print("Opcion invalida")

while True:
    op=int(input('''
Ingrese una opcion:
                 1. iniciar sesion
                 2. registrar
                 3. salir
'''))
    match op:
        case 1:
            inicio()
        case 2:
            registro()
        case 3:
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")