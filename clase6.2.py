alumnos=int(input("Ingrese la cantidad de alumnos que hay: "))
total=0
totalg=0
for i in range(1,alumnos+1):
    print(f"Alumno {i}")
    cant_notas=int(input(f"Ingrese cantidad de notas del alumno {i}: "))
    total=0
    for c in range(1,cant_notas+1):
        notas=float(input(f"Ingrese la nota {c} del alumno {i}: "))
        total=total+notas
    prom=total/cant_notas
    totalg=totalg+prom
promg=totalg/alumnos
print(f"El total es ", promg)
        
