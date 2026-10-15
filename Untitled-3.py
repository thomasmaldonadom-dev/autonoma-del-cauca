trabajadores = int(input("Ingrese la cantidad de trabajadores: "))

salarios_A = []
edades_A = []

salarios_B = []
edades_B = []

salarios_C = []
edades_C = []

for i in range(trabajadores):
    print(f"\nTrabajador {i + 1}")

    salario = float(input("Salario mensual: "))
    antiguedad = float(input("Antigüedad en años: "))
    edad = int(input("Edad: "))

    if 0 <= antiguedad <= 2:
        salarios_A.append(salario)
        edades_A.append(edad)
    elif antiguedad > 2 and antiguedad <= 8:
        salarios_B.append(salario)
        edades_B.append(edad)
    elif antiguedad > 8:
        salarios_C.append(salario)
        edades_C.append(edad)

for nombre in ["A", "B", "C"]:
    if nombre == "A":
        salarios = salarios_A
        edades = edades_A
    elif nombre == "B":
        salarios = salarios_B
        edades = edades_B
    else:
        salarios = salarios_C
        edades = edades_C

    print(f"\nGrupo {nombre}")

    cantidad = len(salarios)

    if cantidad > 0:
        suma_salarios = sum(salarios)
        promedio_salario = suma_salarios / cantidad
        promedio_edad = sum(edades) / cantidad
    else:
        promedio_salario = 0
        suma_salarios = 0
        promedio_edad = 0

    if nombre == "A":
        if promedio_salario > 2000000:
            incremento = 4
        else:
            incremento = 7

    elif nombre == "B":
        if promedio_salario > 2400000:
            incremento = 5
        else:
            incremento = 8

    else:
        if promedio_salario > 3000000:
            incremento = 6
        else:
            incremento = 10

    print("Cantidad de trabajadores:", cantidad)
    print("Promedio de salarios:", promedio_salario)
    print("Suma total de salarios:", suma_salarios)
    print("Promedio de edades:", promedio_edad)
    print("Incremento anual:", incremento, "%")