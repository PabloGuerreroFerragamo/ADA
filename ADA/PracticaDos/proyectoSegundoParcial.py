# Importa la biblioteca NumPy para trabajar con matrices y operaciones numéricas
import numpy as np

# Define la función para encontrar la asignación óptima de objetos a dos mochilas
def asignacion_mochilas_optima(objetos, costos_mochila1, beneficios_mochila1, costos_mochila2, beneficios_mochila2, presupuesto_mochila1, presupuesto_mochila2):
    # Obtiene la cantidad total de objetos
    n = len(objetos)
    # Asegura que los presupuestos de ambas mochilas sean valores enteros
    presupuesto_mochila1 = int(presupuesto_mochila1)
    presupuesto_mochila2 = int(presupuesto_mochila2)

    # Crea una matriz para almacenar los beneficios máximos alcanzados
    # Dimensiones: (presupuesto_mochila1 + 1) x (presupuesto_mochila2 + 1)
    MatrizValores = np.zeros((presupuesto_mochila1 + 1, presupuesto_mochila2 + 1))
    # Crea un diccionario para registrar las decisiones de asignación de cada objeto
    seleccion = {}

    # Itera sobre cada objeto
    for i in range(n):
        # Extrae los costos y beneficios del objeto actual para ambas mochilas
        costo1, beneficio1 = costos_mochila1[i], beneficios_mochila1[i]
        costo2, beneficio2 = costos_mochila2[i], beneficios_mochila2[i]
        # Crea una copia de la matriz actual para actualizarla en esta iteración
        nuevo_MatrizValores = MatrizValores.copy()

        # Recorre los presupuestos de la mochila 1 de mayor a menor
        for j in range(presupuesto_mochila1, -1, -1):
            # Recorre los presupuestos de la mochila 2 de mayor a menor
            for k in range(presupuesto_mochila2, -1, -1):
                # Verifica si el objeto puede ser asignado a la mochila 1
                if j >= costo1:
                    # Calcula el beneficio que se obtendría si el objeto se asigna a la mochila 1
                    nuevo_beneficio = MatrizValores[j - costo1][k] + beneficio1
                    # Si este beneficio es mayor al beneficio actual, lo actualiza
                    if nuevo_beneficio > nuevo_MatrizValores[j][k]:
                        nuevo_MatrizValores[j][k] = nuevo_beneficio
                        # Registra la asignación del objeto a la mochila 1
                        seleccion[(i, j, k)] = 'Mochila1'

                # Verifica si el objeto puede ser asignado a la mochila 2
                if k >= costo2:
                    # Calcula el beneficio que se obtendría si el objeto se asigna a la mochila 2
                    nuevo_beneficio = MatrizValores[j][k - costo2] + beneficio2
                    # Si este beneficio es mayor al beneficio actual, lo actualiza
                    if nuevo_beneficio > nuevo_MatrizValores[j][k]:
                        nuevo_MatrizValores[j][k] = nuevo_beneficio
                        # Registra la asignación del objeto a la mochila 2
                        seleccion[(i, j, k)] = 'Mochila2'

        # Actualiza la matriz principal con los valores de esta iteración
        MatrizValores = nuevo_MatrizValores

    # Inicializa los presupuestos restantes para rastrear las asignaciones óptimas
    j, k = presupuesto_mochila1, presupuesto_mochila2
    # Crea un diccionario para almacenar las asignaciones finales de cada mochila
    asignaciones = {'Mochila1': [], 'Mochila2': []}
    # Lista para registrar los objetos que no se asignaron a ninguna mochila
    objetos_no_asignados = []

    # Retrocede sobre los objetos para determinar las asignaciones óptimas
    for i in range(n - 1, -1, -1):
        # Verifica si el objeto fue asignado a alguna mochila
        if (i, j, k) in seleccion:
            # Si se asignó a la mochila 1
            if seleccion[(i, j, k)] == 'Mochila1':
                asignaciones['Mochila1'].append((objetos[i], beneficios_mochila1[i]))
                # Reduce el presupuesto de la mochila 1
                j -= costos_mochila1[i]
            # Si se asignó a la mochila 2
            elif seleccion[(i, j, k)] == 'Mochila2':
                asignaciones['Mochila2'].append((objetos[i], beneficios_mochila2[i]))
                # Reduce el presupuesto de la mochila 2
                k -= costos_mochila2[i]
        else:
            # Si el objeto no se asignó, se agrega a la lista de no asignados
            objetos_no_asignados.append(objetos[i])

    # Obtiene el beneficio máximo alcanzado desde la matriz
    valor_maximo_beneficio = MatrizValores[presupuesto_mochila1][presupuesto_mochila2]
    # Devuelve el beneficio máximo, las asignaciones finales y los objetos no asignados
    return valor_maximo_beneficio, asignaciones, objetos_no_asignados

# Lista de objetos a asignar
objetos = ["Banner Estático", "Banner Interactivo", "Video Corto", "Video Largo", "Pop-Up",
           "Anuncio en Carrusel", "Anuncio en Historias", "Anuncio de Búsqueda", "Anuncio Nativo",
           "Anuncio de Display Programático"]

# Costos y beneficios de los objetos para la mochila 1
costos_mochila1 = [200, 300, 250, 400, 150, 350, 220, 250, 180, 320]
beneficios_mochila1 = [300, 500, 450, 650, 250, 550, 400, 350, 300, 600]

# Costos y beneficios de los objetos para la mochila 2
costos_mochila2 = [250, 350, 300, 450, 200, 400, 280, 300, 230, 370]
beneficios_mochila2 = [350, 600, 550, 750, 300, 650, 450, 500, 350, 700]

# Presupuestos disponibles para cada mochila
presupuesto_mochila1 = 1000
presupuesto_mochila2 = 1200

# Llama a la función con los datos de ejemplo
valor_maximo_beneficio, asignaciones, objetos_no_asignados = asignacion_mochilas_optima(
    objetos, costos_mochila1, beneficios_mochila1, costos_mochila2, beneficios_mochila2, presupuesto_mochila1, presupuesto_mochila2)

# Imprime el beneficio máximo alcanzado
print(f"Valor máximo de beneficio: {valor_maximo_beneficio}")

# Imprime los objetos asignados a la mochila 1
print("\nAsignación de objetos a Mochila 1:")
for objeto, beneficio in asignaciones['Mochila1']:
    print(f"- {objeto}: {beneficio} beneficios")

# Imprime los objetos asignados a la mochila 2
print("\nAsignación de objetos a Mochila 2:")
for objeto, beneficio in asignaciones['Mochila2']:
    print(f"- {objeto}: {beneficio} beneficios")

# Imprime los objetos que no se asignaron a ninguna mochila
print("\nObjetos no asignados a ninguna mochila:")
if objetos_no_asignados:
    for objeto in objetos_no_asignados:
        print(f"- {objeto}")
else:
    print("No hay objetos no asignados.")
