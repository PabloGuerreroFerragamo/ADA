def elKuromi(pesoMax, beneficio, pesoObjeto, Vop, decisiones):
    for objeto in range(1, len(beneficio) + 1):
        for pesoActual in range(0, pesoMax + 1):
            if pesoObjeto[objeto - 1] <= pesoActual:
                sin_incluir = Vop[objeto - 1][pesoActual]
                incluir = beneficio[objeto - 1] + Vop[objeto - 1][pesoActual - pesoObjeto[objeto - 1]]

                # Guardamos el máximo valor y la decisión
                if incluir > sin_incluir:
                    Vop[objeto][pesoActual] = incluir
                    decisiones[objeto][pesoActual] = True  # Se incluyó el objeto
                else:
                    Vop[objeto][pesoActual] = sin_incluir
                    decisiones[objeto][pesoActual] = False  # No se incluyó el objeto
            else:
                Vop[objeto][pesoActual] = Vop[objeto - 1][pesoActual]
                decisiones[objeto][pesoActual] = False  # No se puede incluir el objeto


def rastrear_objetos(pesoMax, pesoObjeto, decisiones):
    objetos_seleccionados = []
    pesoActual = pesoMax
    objeto = len(pesoObjeto)

    while objeto > 0 and pesoActual > 0:
        if decisiones[objeto][pesoActual]:  # Si se incluyó el objeto
            objetos_seleccionados.append(objeto - 1)  # Guardamos el índice del objeto
            pesoActual -= pesoObjeto[objeto - 1]
        objeto -= 1

    return objetos_seleccionados


# Datos del problema
pesoMax = 5
beneficio = [10, 20, 30]
peso = [2, 1, 4]

# Inicializar la matriz de valores óptimos y decisiones
matriz = [[0] * (pesoMax + 1) for _ in range(len(peso) + 1)]
decisiones = [[False] * (pesoMax + 1) for _ in range(len(peso) + 1)]

# Imprimir la matriz inicial
print("Matriz inicial:")
for fila in matriz:
    print(fila)

# Llenar la matriz con los valores óptimos
elKuromi(pesoMax, beneficio, peso, matriz, decisiones)

# Imprimir la matriz final
print("\nMatriz final:")
for fila in matriz:
    print(fila)

# Realizar el rastreo para encontrar los objetos seleccionados
objetos_seleccionados = rastrear_objetos(pesoMax, peso, decisiones)
print("\nObjetos seleccionados:", objetos_seleccionados)
