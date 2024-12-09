import numpy as np

def LLenaMochila(pesoMax, ObjetosT, Beneficios, Pesos, ObjetosDisponibles):
    TablaValores = np.zeros((ObjetosT+1, pesoMax+1))
    TablaBin = np.zeros((ObjetosT+1, pesoMax+1))

    for obj in range(1, ObjetosT+1):
        if not ObjetosDisponibles[obj-1]:  # Saltar si el objeto no está disponible
            continue
        for w in range(1, pesoMax+1):
            if Pesos[obj-1] <= w:
                TablaValores[obj][w] = max(
                    TablaValores[obj-1][w],
                    Beneficios[obj-1] + TablaValores[obj-1][w-Pesos[obj-1]]
                )
                if TablaValores[obj-1][w] < Beneficios[obj-1] + TablaValores[obj-1][w-Pesos[obj-1]]:
                    TablaBin[obj][w] = 1
            else:
                TablaValores[obj][w] = TablaValores[obj-1][w]

    # Depuración: Mostrar las tablas finales
    print(f"Tabla de valores:\n{TablaValores}")
    print(f"Tabla binaria:\n{TablaBin}")

    W = pesoMax
    ObjetosSeleccionados = []
    for obj in range(ObjetosT, 0, -1):
        if TablaBin[obj][W] == 1:
            ObjetosSeleccionados.append(obj)
            W -= Pesos[obj-1]

    # Depuración: Mostrar los objetos seleccionados y su beneficio
    print(f"Objetos seleccionados en esta mochila: {ObjetosSeleccionados}")
    beneficio_total = sum(Beneficios[obj-1] for obj in ObjetosSeleccionados)
    print(f"Beneficio total: {beneficio_total}")

    return beneficio_total, ObjetosSeleccionados

PresupMax = [1000, 1200]
NumMochilas = 2
ObjetosT = 10
Ventas = [
    [300, 500, 450, 650, 250, 550, 400, 350, 300, 600],
    [350, 600, 550, 750, 300, 650, 450, 500, 350, 700]
]
Costos = [
    [200, 300, 250, 400, 150, 350, 220, 250, 180, 320],
    [250, 350, 300, 450, 200, 400, 280, 300, 230, 370]
]

ObjetosDisponibles = [True] * ObjetosT
ObjetosPorMochila = []

for i in range(NumMochilas):
    print(f"\nLlenando mochila {i+1} con presupuesto máximo {PresupMax[i]}...")
    Beneficios = Ventas[i]
    Pesos = Costos[i]
    beneficio, objetosSeleccionados = LLenaMochila(PresupMax[i], ObjetosT, Beneficios, Pesos, ObjetosDisponibles)
    ObjetosPorMochila.append((beneficio, objetosSeleccionados))

    # Actualizar disponibilidad de objetos
    for obj in objetosSeleccionados:
        ObjetosDisponibles[obj-1] = False

    # Depuración: Mostrar disponibilidad de objetos después de esta mochila
    print(f"Disponibilidad después de mochila {i+1}: {ObjetosDisponibles}")

# Resultados finales
for i, (beneficio, objetos) in enumerate(ObjetosPorMochila):
    print(f"Mochila {i+1}: Beneficio = {beneficio}, Objetos = {objetos}")
