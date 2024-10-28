aprobados = 0
suspensos = 0

for i in range (10):

    nota = int(input(f"Ingrese calificación del alumno {i+1}:\n"))

    if nota >= 7:
        aprobados += 1
    else:
        suspensos += 1

print(f"Cantidad de alumnos con nota mayor o igual a 7: {aprobados}")
print(f"Cantidad de alumnos suspensos: {suspensos}")