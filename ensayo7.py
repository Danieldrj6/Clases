biblioteca = [
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "genero": "Realismo mágico",
        "ejemplares": 4
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "año": 1949,
        "genero": "Distopía",
        "ejemplares": 2
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605,
        "genero": "Novela",
        "ejemplares": 1
    }
]

def mostrar():
    for libros in biblioteca:
        print(f'''Libro titulado: {libros["titulo"]}
Autor: {libros["autor"]}
Lanzado en: {libros["año"]}
Genero: {libros["genero"]}
Stock: {libros["ejemplares"]}
''')

def validar_fecha(fecha):
    return len(fecha) == 4 and fecha.isdigit()

def validar_stock(stock):
    return stock > 0 and stock.isdigit()

def agregar():
    titulo = input("Ingrese el nombre del ejemplar: ")
    autor = input("Ingrese el autor: ")
    fecha = input("Ingrese fecha de lanzamiento: ")
    while not validar_fecha(fecha):
        print("ERROR")
        fecha = input("Ingrese fecha de lanzamiento: ")
    genero = input("Ingrese genero del libro: ")
    stock = input("Cual es el stock inicial?: ")
    while not validar_stock(stock):
        print("ERROR")
        stock = input("Cual es el stock inicial?: ")
    nuevo_libro = {
        "titulo":titulo,
        "autor":autor,
        "año":fecha,
        "genero":genero,
        "ejemplares":stock
    }
    biblioteca.append(nuevo_libro)
    mostrar()
agregar()

