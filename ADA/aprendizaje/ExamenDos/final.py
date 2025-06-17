# Inicialización
Nnodos = 8
nodos = {'A': [('B', 1), ('C', 4)],
         'B': [('A', 1), ('C', 3), ('D', 3), ('E', 5)],
         'C': [('A', 4), ('B', 3), ('E', 3), ('F', 1)],
         'D': [('B', 3), ('E', 1), ('G', 2)],
         'E': [('B', 5), ('C', 3), ('D', 1), ('F', 1)],
         'F': [('C', 1), ('E', 1), ('H', 3)],
         'G': [('D', 2), ('H', 1)],
         'H': [('G', 1)]}

infinito = float('inf')

# Distancias iniciales
dist = {'A': 0, 'B': infinito, 'C': infinito, 'D': infinito,
        'E': infinito, 'F': infinito, 'G': infinito, 'H': infinito}

# Predecesores inicializados
predecesor = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
              'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H'}

# Nodos no visitados
Nnovisitados = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Nodo inicial y final
posicion = 'A'
final = 'H'

# Mientras existan elementos en Nnovisitados
while Nnovisitados:
    # Inicializar el vecino de costo mínimo
    vecino_min = None
    costo_min = infinito

    # Recorrer todos los vecinos de posición
    for vecino, costo in nodos[posicion]:
        if vecino in Nnovisitados:
            # Actualizar el mínimo costo desde cada una de las rutas
            nueva_dist = dist[posicion] + costo
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                predecesor[vecino] = posicion

    # Encontrar el vecino de costo mínimo para la próxima posición
    for nodo in Nnovisitados:
        if dist[nodo] < costo_min:
            costo_min = dist[nodo]
            vecino_min = nodo

    # Si no hay vecino válido, terminamos
    if vecino_min is None:
        break

    # Eliminar el nodo que ya visitó a todos sus vecinos
    Nnovisitados.remove(vecino_min)

    # Avanzar a la próxima posición de los vecinos
    posicion = vecino_min

    # Si llegamos al nodo final, terminamos
    if posicion == final:
        break

# Reconstruir la ruta más corta
ruta = []
nodo_actual = final
while nodo_actual != predecesor[nodo_actual]:  # Condición para detenerse
    ruta.insert(0, nodo_actual)
    nodo_actual = predecesor[nodo_actual]
ruta.insert(0, nodo_actual)  # Agregar el nodo inicial

# Resultado
print("Distancia mínima de 'A' a 'H':", dist[final])
print("Ruta más corta:", " -> ".join(ruta))
