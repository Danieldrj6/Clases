notas = []

while True:
    op=int(input('''
    Seleccione una opcion:
        1. Ingresar notas
        2. borrar nota
        3. mostrar notas
        4. sacar promedio, nota mayor y menor
        5. limpiar lista de notas
        6. salir
'''))
    match op:
        case 1:
            cant_notas=int(input("Ingrese cantidad de notas a ingresar: "))
            for i in range(cant_notas):
                nota_extra=float(input(f"Ingrese nota {i+1}: "))
                notas.append(nota_extra)
        case 2:
            c=0
            for nota in notas:
                print("opcion:",(c+1), " ", notas[c])
                c+=1
            nota_borrar=int(input("Que nota desea borrar?: "))
            notas.pop(nota_borrar-1)
        case 3:
            for nota in notas:
                print(nota)
        case 4:
            c=0
            suma=0
            for nota in notas:
                suma=suma+nota
                c+=1
            prom=suma/len(notas)
            print(prom)
            nota_alta = max(notas)
            nota_baja = min(notas)
            print(f"La nota mas alta es: {nota_alta} y la mas baja es {nota_baja}")
        case 5:
            notas.clear()
            print("Notas borradas!")
        case 6:
            print("Saliendo")
            break