
pokedex = [
    {"nombre": "Charmander",
  "tipo": "Fuego",
  "nivel": 12,
  "ataques": ["Ascuas", "Arañazo", "Pantalla de humo"]}
]

def validar_nombre(nombre):
    nombre = nombre.strip().lower()
    if not nombre:
        return False
    for pokemon in pokedex:
        if pokemon["nombre"].lower() == nombre:
            return False
    return True

def validar_tipo(tipo):
    tipo = tipo.strip().lower()
    tipos_validos = [
        "acero", "agua", "bicho", "dragon", "electrico", "fantasma", "fuego",
        "hada", "hielo", "lucha", "normal", "planta", "psiquico",
        "roca", "siniestro", "tierra", "veneno", "volador"
    ]
    if not tipo:
        return False
    if tipo not in tipos_validos:
        return False
    return True

def validar_nivel(nivel):
    if not nivel.isdigit():
        return False
    if nivel > 100:
        return False

        return False
    return True

def registro():
    while True:
        nombre = input("Ingrese el nombre del pokemon!: ").strip().lower()
        if validar_nombre(nombre):
            break
        else:
            print("ERROR")
    while True:
        tipo = input("Ingrese el tipo de pokemon!: ").strip().lower()
        if validar_tipo(tipo):
            break
        else:
            print("Tipo inexistente")
    while True:
        nivel = int(input("Ingrese nivel del pokemon: "))
        if validar_nivel(nivel):
            break
        else:
            print("Nivel erroneo")
registro()


