import random as rd

# nombre="Daniel"
# edad=20
# print("Hola", nombre, "tu edad es de", edad)

# nombre=str(input("Escribe tu nombre: "))
# edad=int(input("Escribe tu edad: "))
# print("Hola", nombre, "tu edad es de", edad)


"""
clave_correcta="1234"
usuario_correcto="Daniel"
usuario=str(input("Escribe tu usuario: "))
clave=str(input("Escribe tu clave: "))
if usuario==usuario_correcto and clave==clave_correcta:
    print("Bienvenido", usuario, "Usted ha iniciado sesión")
else:
    print("Usuario o clave incorrecta")

dado=rd.randint(1,6)
print("Tirando el dado...")
print("El numero es", dado)
"""


dinero=1000
while dinero>0:
    apuesta=int(input("Cuanto dinero quieres apostar? "))
    if apuesta>dinero:
        print("No puedes apostar mas de lo que tienes")
        input("Presiona enter para girar la ruleta")
        ruleta=rd.randint(0,36)
        print("Tirando la ruleta...")
    if ruleta==1:
        print("Ganaste la apuesta ya que salio el 1")
        dinero=dinero+apuesta*2
    else:
        print("Perdiste la apuesta ya que salio el", ruleta)
        dinero=dinero-apuesta
        print("Tu dinero ahora es de", dinero)


# print("Hola mundo!")

"""
Caracter es str o string
numeros es int o integer
verdadero o falso es booleano o bool o boolean
decimales es float
"""