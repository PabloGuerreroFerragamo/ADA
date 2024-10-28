def merge(DatosIzq, DatosDer, ListaIzq, ListaDer):
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

    # Agrega los elementos restantes
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
    return merge(DatosIzq, DatosDer, ListaIzq, ListaDer)

Lista1 = [5, 4, 3, 2, 1]
Lista2 = [3, 1, 4, 2, 5]

# Ordenar Lista1 y reordenar Lista2 según el orden de Lista1
Arreglo1, Arreglo2 = mergesort(Lista1, Lista2)

print("Lista1 ordenada:", Arreglo1)
print("Lista2 ordenada:", Arreglo2)