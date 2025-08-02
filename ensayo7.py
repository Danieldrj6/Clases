biblioteca = [
    {
        "titulo": "cien años de soledad",
        "autor": "gabriel garcia marquez",
        "año": 1967,
        "genero": "realismo magico",
        "ejemplares": 4
    },
    {
        "titulo": "1984",
        "autor": "george orwell",
        "año": 1949,
        "genero": "distopia",
        "ejemplares": 2
    },
    {
        "titulo": "don quijote de la mancha",
        "autor": "miguel de cervantes",
        "año": 1605,
        "genero": "novela",
        "ejemplares": 1
    }
]

def mostrar():
    c = 1
    for libros in biblioteca:
        print(f'''ID: {c}: Libro titulado: {libros["titulo"]}
Autor: {libros["autor"]}
Lanzado en: {libros["año"]}
Genero: {libros["genero"]}
Stock: {libros["ejemplares"]}
''')
        c+=1

def validar_fecha(fecha):
    return len(fecha) == 4 and fecha.isdigit()

def validar_stock(stock):
    return stock.isdigit() and int(stock) > 0

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

def buscar():
    busqueda = input("Ingrese autor a buscar: ")
    for libros in biblioteca:
        autor = libros["autor"]
        if busqueda.lower() not in libros["autor"]:
            print("")
        else:
            if busqueda.lower() == autor:
                print(f'''Libro titulado: {libros["titulo"]}
Autor: {autor}
Lanzado en: {libros["año"]}
Genero: {libros["genero"]}
Stock: {libros["ejemplares"]}
''')

def buscar_genero():
    busqueda = input("Ingrese genero a buscar: ")
    for libros in biblioteca:
        genero = libros["genero"]
        if busqueda.lower() not in libros["genero"]:
            print("")
        else:
            if busqueda.lower() == genero:
                print(f'''Libro titulado: {libros["titulo"]}
Autor: {libros["autor"]}
Lanzado en: {libros["año"]}
Genero: {libros["genero"]}
Stock: {libros["ejemplares"]}
''')

def ejemplares():
    mostrar()
    seleccion = int(input("Ingrese numero del libro a actualizar: "))
    nuevo_stock = int(input("Ingrese stock total: "))
    biblioteca[seleccion-1]["ejemplares"] = nuevo_stock
    mostrar()


while True:
    op = int(input('''
Ingrese opcion:
                   1. Mostrar libros
                   2. Agregar libros
                   3. Buscar por autor
                   4. Buscar por genero
                   5. Actualizar ejemplares
                   6. Salir
'''))
    match op:
        case 1:
            mostrar()
        case 2:
            agregar()
        case 3:
            buscar()
        case 4:
            buscar_genero()
        case 5:
            ejemplares()
        case 6:
            print("Saliendo...")
            break
        case _:
            print("ERROR")