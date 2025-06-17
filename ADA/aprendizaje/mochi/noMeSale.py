def valorOptimo(beneficio, pesoObjeto, pesoMax, Vop):
    for pesoActual in range(0, pesoMax + 1):
        for objeto in range(0, len(pesoObjeto)):
            if pesoObjeto[objeto] <= pesoActual:
                if objeto > 0:
                    Vop[objeto][pesoActual] = max(
                        beneficio[objeto] + Vop[objeto - 1][pesoActual - pesoObjeto[objeto]],
                        Vop[objeto - 1][pesoActual]
                    )
                else:
                    Vop[objeto][pesoActual] = beneficio[objeto]
            else:
                if objeto > 0:
                    Vop[objeto][pesoActual] = Vop[objeto - 1][pesoActual]
                else:
                    Vop[objeto][pesoActual] = 0  # No se incluye el objeto

# Datos de entrada
pesoMax = 5
beneficio = [10, 20, 30]
peso = [2, 1, 4]

# Inicializar la matriz Vop con dimensiones (len(peso)+1) x (pesoMax+1)
matriz = [[0] * (pesoMax + 1) for _ in range(len(peso) + 1)]

# Mostrar matriz inicial
print("Matriz inicial:")
for fila in matriz:
    print(fila)

# Llamar a la función
valorOptimo(beneficio, peso, pesoMax, matriz)

# Mostrar la matriz final
print("\nMatriz final:")
for fila in matriz:
    print(fila)
