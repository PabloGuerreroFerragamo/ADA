from re import I
import openpyxl
import math

libro = openpyxl.load_workbook('Dataset del Tracklist.xlsx')  # se abre el archivo para poder manipular su contenido
hoja = libro.active  # hoja devolverá la primera hoja de nuestro libro

rangosALeer = ['C2:M2', 'C3:M3', 'C4:M4', 'C5:M5', 'C6:M6', 'C7:M7', 'C8:M8', 'C9:M9', 'C10:M10',
               'C11:M11', 'C12:M12', 'C13:M13', 'C14:M14', 'C15:M15', 'C16:M16', 'C17:M17', 'C18:M18', 'C19:M19',
               'C20:M20', 'C21:M21', 'C22:M22', 'C23:M23', 'C24:M24', 'C25:M25', 'C26:M26', 'C27:M27', 'C28:M28', 'C29:M29',
               'C30:M30', 'C31:M31', 'C32:M32', 'C33:M33', 'C34:M34', 'C35:M35', 'C36:M36']

arreglos = [None] * len(rangosALeer)

for i in range(len(rangosALeer)):
    rangoHorizontal = hoja[rangosALeer[i]]
    arregloGuardador = [None] * len(rangoHorizontal[0])

    for j in range(len(rangoHorizontal[0])):
        arregloGuardador[j] = rangoHorizontal[0][j].value

    arreglos[i] = arregloGuardador

def MergeSortRemap(DatosIzq, DatosDer, ListaIzq, ListaDer):
    i = j = 0
    mergedA = []
    mergedB = []

    while i < len(DatosIzq) and j < len(DatosDer):
        if DatosIzq[i] < DatosDer[j]:
            mergedA.append(DatosIzq[i])
            mergedB.append(ListaIzq[i])
            i += 1
        else:
            mergedA.append(DatosDer[j])
            mergedB.append(ListaDer[j])
            j += 1

    mergedA.extend(DatosIzq[i:])
    mergedB.extend(ListaIzq[i:])
    mergedA.extend(DatosDer[j:])
    mergedB.extend(ListaDer[j:])

    return mergedA, mergedB

def mergesort(Datos, Lista):
    if len(Datos) <= 1:
        return Datos, Lista
    mid = len(Datos) // 2
    DatosIzq, ListaIzq = mergesort(Datos[:mid], Lista[:mid])
    DatosDer, ListaDer = mergesort(Datos[mid:], Lista[mid:])
    return MergeSortRemap(DatosIzq, DatosDer, ListaIzq, ListaDer)

cont = [0] * len(rangosALeer)

def MergeSortCount(Dat):
    if len(Dat) <= 1:
        return Dat, 0  # Retorna la lista y 0 inversiones si tiene 1 o menos elementos

    mid = len(Dat) // 2
    # Divide y cuenta las inversiones en cada mitad
    left, left_inv = MergeSortCount(Dat[:mid])
    right, right_inv = MergeSortCount(Dat[mid:])

    # Fusión de las mitades y cuenta de inversiones cruzadas
    merged, cross_inv = merge_and_count(left, right)

    # Suma de inversiones de cada mitad y de las cruzadas
    total_inv = left_inv + right_inv + cross_inv
    return merged, total_inv

def merge_and_count(left, right):
    merged = []
    i = j = 0
    inversions = 0

    # Fusiona las dos mitades ordenadas
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # Cuenta las inversiones: todos los elementos restantes en `left` son mayores
            inversions += len(left) - i

    # Agrega los elementos restantes
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

# Ahora puedes contar las inversiones en Arreglo2 correctamente
Inversiones = [[0] * len(arreglos) for _ in range(len(arreglos))]
for i in range(len(rangosALeer)):
    for j in range(len(arreglos)):
        Lista1 = arreglos[i]
        Lista2 = arreglos[j]
        Arreglo1, Arreglo2 = mergesort(Lista1, Lista2)

        print(f"Estudiante {i+1} ordenada: {Arreglo1} Estudiante {j+1} ordenada: {Arreglo2}")

        # Contar inversiones en Arreglo2
        _, inversionesArreglo2 = MergeSortCount(Arreglo2)  # Ignoramos el arreglo ordenado y solo obtenemos el conteo
        print(f"Inversiones en Arreglo2: {inversionesArreglo2}")
        Inversiones[i][j] = inversionesArreglo2

def promedio(matriz):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            suma = matriz[i][j]+suma
    return suma/(len(matriz)*len(matriz[0]))


def calcular_desviacion_estandar(matriz):
    # Calcular la cantidad de elementos y la suma total
    elementos = [elem for fila in matriz for elem in fila]
    cantidad = len(elementos)
    suma_total = sum(elementos)

    # Calcular el promedio
    promedio = suma_total / cantidad

    # Calcular la suma de las diferencias al cuadrado respecto al promedio
    suma_diferencias_cuadradas = sum((x - promedio) ** 2 for x in elementos)

    # Calcular la desviación estándar
    desviacion_estandar = math.sqrt(suma_diferencias_cuadradas / cantidad)

    return desviacion_estandar


print("La desviación estándar es:", calcular_desviacion_estandar(Inversiones))


#print(Inversiones)
print(promedio(Inversiones))