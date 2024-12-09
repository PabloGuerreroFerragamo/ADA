import numpy as np

def asignacion_mochilas_optima(objetos, costos_mochila1, beneficios_mochila1, costos_mochila2, beneficios_mochila2, presupuesto_mochila1, presupuesto_mochila2):
    n = len(objetos)#cantidad total de elementos

    # verificamos que el presupuesto sea int
    presupuesto_mochila1 = int(presupuesto_mochila1)
    presupuesto_mochila2 = int(presupuesto_mochila2)

    #se asigna una matriz de ceros, con filas y columnas como parametros
    MatrizValores = np.zeros((presupuesto_mochila1 + 1, presupuesto_mochila2 + 1))
    seleccion = {}#se crea diccionario para las selecciones

    for i in range(n):#i va de 0 a n sin llegar a n
        #asignamos los costos y beneficios del objeto actual (i)
        costo1, beneficio1 = costos_mochila1[i], beneficios_mochila1[i]
        costo2, beneficio2 = costos_mochila2[i], beneficios_mochila2[i]
        nuevo_MatrizValores = MatrizValores.copy()#creamos una copia de la matriz

        for j in range(presupuesto_mochila1, -1, -1):#recorremos el presupuesto_mochila 1, de mayor a menor
            for k in range(presupuesto_mochila2, -1, -1):#recorremos el presupuesto_mochila 2, de mayor a menor

                #se verifica si el objeto puede ser asignado a la mochila 1
                if j >= costo1:#si el presupuesto actual es mayor o igual al costo1
                    nuevo_beneficio = MatrizValores[j - costo1][k] + beneficio1#beneficio que se obtendría si el objeto se asigna a la mochila 1
                    if nuevo_beneficio > nuevo_MatrizValores[j][k]:#si este beneficio es mayor al beneficio actual
                        nuevo_MatrizValores[j][k] = nuevo_beneficio#actualizamos el beneficio maximo
                        seleccion[(i, j, k)] = 'Mochila1'#se guarda en seleccion que el objeto i fue asignado en mochila1, con presupuesto i,j

                #se verifica si el objeto puede ser asignado a la mochila 2
                if k >= costo2:
                    nuevo_beneficio = MatrizValores[j][k - costo2] + beneficio2
                    if nuevo_beneficio > nuevo_MatrizValores[j][k]:
                        nuevo_MatrizValores[j][k] = nuevo_beneficio
                        seleccion[(i, j, k)] = 'Mochila2'

        MatrizValores = nuevo_MatrizValores#se actualiza la matriz principal con los valores de esta iteración


    j, k = presupuesto_mochila1, presupuesto_mochila2#inicializamos i,j con los presupuestos
    asignaciones = {'Mochila1': [], 'Mochila2': []}#creamos un diccionario, donde se guardaran los objetos, junto con su beneficio en su mochila correspondiente
    objetos_no_asignados = []#arreglo de objetos no guardados

    #se regresa sobre los objetos para determinar las asignaciones óptimas
    for i in range(n - 1, -1, -1):
        if (i, j, k) in seleccion:
            if seleccion[(i, j, k)] == 'Mochila1':
                asignaciones['Mochila1'].append((objetos[i], beneficios_mochila1[i]))
                j -= costos_mochila1[i]
            elif seleccion[(i, j, k)] == 'Mochila2':
                asignaciones['Mochila2'].append((objetos[i], beneficios_mochila2[i]))
                k -= costos_mochila2[i]
        else:
            objetos_no_asignados.append(objetos[i])

    #beneficio máximo alcanzado desde la matriz
    valor_maximo_beneficio = MatrizValores[presupuesto_mochila1][presupuesto_mochila2]
    return valor_maximo_beneficio, asignaciones, objetos_no_asignados

#datos
objetos = ["Banner Estático", "Banner Interactivo", "Video Corto", "Video Largo", "Pop-Up", "Anuncio en Carrusel", "Anuncio en Historias", "Anuncio de Busqueda", "Anuncio Nativo", "Anuncio de Display Programatico"]
costos_mochila1 = [200, 300, 250, 400, 150, 350, 220, 250, 180, 320]
beneficios_mochila1 = [300, 500, 450, 650, 250, 550, 400, 350, 300, 600]
costos_mochila2 = [250, 350, 300, 450, 200, 400, 280, 300, 230, 370]
beneficios_mochila2 = [350, 600, 550, 750, 300, 650, 450, 500, 350, 700]

presupuesto_mochila1 = 1000
presupuesto_mochila2 = 1200

#llamamos a nuestra funcion
valor_maximo_beneficio, asignaciones, objetos_no_asignados = asignacion_mochilas_optima(
    objetos, costos_mochila1, beneficios_mochila1, costos_mochila2, beneficios_mochila2, presupuesto_mochila1, presupuesto_mochila2)

print(f"Valor máximo de beneficio: {valor_maximo_beneficio}")

print("\nAsignación de objetos a Mochila 1:")
for objeto, beneficio in asignaciones['Mochila1']:
    print(f"- {objeto}: {beneficio} beneficios")

print("\nAsignación de objetos a Mochila 2:")
for objeto, beneficio in asignaciones['Mochila2']:
    print(f"- {objeto}: {beneficio} beneficios")

print("\nObjetos no asignados a ninguna mochila:")
if objetos_no_asignados:
    for objeto in objetos_no_asignados:
        print(f"- {objeto}")
else:
    print("No hay objetos no asignados.")