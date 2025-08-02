# class libro:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.paginas = paginas

#     def mostrar(self):
#         print(f"Libro: {self.titulo} del autor {self.autor} / {self.paginas} paginas")

#     def es_largo(self):
#         if self.paginas >= 300:
#             return "Es largo"
#         else:
#             return "Es corto"

# libro1 = libro("Tu Mama", "Tu Hermana", 400)
# libro1.mostrar()
# print(f"Tu libro es muy largo? {libro1.es_largo()}")

# import random as rd
# import time as tm

# class Personaje:
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.vida = 100

#     def atacar(self, otro):
#         dano = rd.randint(10, 25)
#         otro.vida -= dano
#         print(f"{self.nombre} ataca a {otro.nombre} y le causa {dano} de dano. {otro.nombre} tiene {otro.vida} de vida")

#     def vivo(self):
#         return self.vida > 0
    
# dinero = 100

# print("Bienvenido al combate mas epico de tu vida!")

# while dinero > 0:

#     jugador1 = Personaje(input("Ingrese nombre del primer jugador: "))
#     jugador2 = Personaje(input("Ingrese nombre del segundo jugador: "))

#     print(f"Tienes {dinero} fichas")

#     apuesta = input("Por quien apuestas? (escribe el nombre): ")
#     apuesta_ficha = int(input("Cuantas fichas deseas apostar?: "))

#     if apuesta_ficha > dinero or apuesta_ficha <= 0:
#         print("Apuesta invalida. Se te otorgaran 10 monedas por defecto")
#         apuesta_ficha = 10

#     turno = 1

#     while jugador1.vivo() and jugador2.vivo():
#         print(f"--- Turno {turno} ---")
#         if turno %2 == 1:
#             jugador1.atacar(jugador2)
#             tm.sleep(2)
#         else:
#             jugador2.atacar(jugador1)
#             tm.sleep(2)
#         turno += 1

#     if jugador1.vivo():
#         print(f"{jugador1.nombre} gana la batalla!")
#         ganador = jugador1.nombre
#     else:
#         print(f"{jugador2.nombre} gana la batalla!")
#         ganador = jugador2.nombre

#     if apuesta == ganador:
#         dinero += apuesta_ficha
#         print(f"Ganaste la apuesta! ahora tienes: {dinero} fichas")
#     else:
#         dinero -= apuesta_ficha
#         print(f"Perdiste la apuesta ademas perdi el juego. Te quedan {dinero} fichas")

# print("\n Juego terminado ya no te quedan monedas..." if dinero <= 0 else "")


import random as rd

# Valores de cartas
valores = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}
 # Creacion de mazo random
def crear_mazo():
    cartas = list(valores.keys())
    mazo = cartas * 4
    rd.shuffle(mazo)
    return mazo

# Creacion del jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def tomar_cartas(self, mazo):
        carta = mazo.pop()
        self.mano.append(carta)
        print(f"{self.nombre} recibe: {carta}")

    def mostrar_mano(self, ocultar_primera=False):
        if ocultar_primera:
            print(f"{self.nombre}: [?] + {self.mano[1:]}")
        else:
            print(f"{self.nombre}: {self.mano} (Total: {self.obtener_valor()})")

    def obtener_valor(self):
        total = 0
        ases = 0
        for carta in self.mano:
            total += valores[carta]
            if carta == "A":
                ases += 1
        while total > 21 and ases:
            total -= 10
            ases -= 1
        return total

    def esta_juego(self):
        return self.obtener_valor() <= 21
    
# Juego principal del blackjack
def jugar():
    fichas = 100
    print(f"Empiezas con {fichas} fichas")
    while fichas > 0:
        print(f"FICHAS DISPONIBLES: {fichas}")
        try:
            apuesta = int(input("Cuanto desea apostar: (0 para salir): "))
        except ValueError:
            print("Entrada invalida")
            continue
        if apuesta == 0:
            print(f"Te retiraste con {fichas} fichas")
            break
        if apuesta > fichas or apuesta <= 0:
            print("Apuesta invalida")
            continue
        mazo = crear_mazo()
        jugador1 = Jugador(input("Ingrese nombre del jugador: "))
        dealer = Jugador("Daniel")

        for _ in range(2):
            jugador1.tomar_cartas(mazo)
            dealer.tomar_cartas(mazo)

        jugador1.mostrar_mano()
        dealer.mostrar_mano(ocultar_primera=True)

        # Turnoss
        while jugador1.esta_juego():
            accion = input("Quieres otra carta? (Hit/Stand): ".lower())
            if accion == "hit":
                jugador1.tomar_cartas(mazo)
                jugador1.mostrar_mano()
            elif accion == "stand":
                break
            else:
                print("Comando invalido compa")
        if not jugador1.esta_juego():
            print("Te jodiste y pasaste del 21")
            fichas -= apuesta
            continue
        
        # Turno del daniii muejeje del dealer
        print(f"Turno del dealer:")
        dealer.mostrar_mano()
        while dealer.obtener_valor() < 16:
            dealer.tomar_cartas(mazo)
            dealer.mostrar_mano()
        
        valor_jugador = jugador1.obtener_valor()
        valor_dealer = dealer.obtener_valor()

        print(f"\nJugador: {valor_jugador} | Dealer Danisin: {valor_dealer}")

        if valor_dealer > 21 or valor_jugador > valor_dealer:
            print("Me ganaste compa")
            fichas += apuesta
        elif valor_jugador == valor_dealer:
            print("Empate")
        else:
            print("Gane muejeje")
            fichas -= apuesta
    if fichas <= 0:
        print("Te quedaste sin fichas... El dani gano.. el danisin siempre gana")

jugar()