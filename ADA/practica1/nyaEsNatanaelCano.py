import openpyxl

libro = openpyxl.load_workbook('Dataset del Tracklist.xlsx')#se abre el archivo para poder manipular su contenido

hoja = libro.active#hoja devolvera la primera hoja de nuestro libro

rangosALeer = ['C2:M2','C3:M3','C4:M4','C5:M5','C6:M6','C7:M7','C8:M8','C9:M9','C10:M10',
               'C11:M11','C12:M12','C13:M13','C14:M14','C15:M15','C16:M16','C17:M17','C18:M18','C19:M19',
               'C20:M20','C21:M21','C22:M22','C23:M23','C24:M24','C25:M25','C26:M26','C27:M27','C28:M28','C29:M29',
               'C30:M30','C31:M31','C32:M32','C33:M33','C34:M34','C35:M35','C36:M36']

arreglos=[None]*len(rangosALeer)

for i in range(0,len(rangosALeer),1):
    rangoHorizontal = hoja[rangosALeer[i]]#hoja recive intervalos de celdas, C3:M3 en i=1
    # rangoHorizontal es toda la fila, la horizontal xd

    #su estructura es rangoHorizontal[0][4], donde el primer[0], indica la fila, la cual es 0, ya que nosotros leemos una sola fila, la primera fila del rango y unica
    #el [4], indica la posicion de la columna

    arregloGuardador=[None]*len(rangoHorizontal[0])#este arreglo tiene la longitud de nuestra fila

    for j in range(0,len(rangoHorizontal[0]),1):#rangoHorizontal en [0], 0 por que indica la fila, la primera del rango y unica, esta mide el largo de la fila, C2, D2, ..., M2
            arregloGuardador[j]=(rangoHorizontal[0][j].value)#obtenemos el valor de cada celda

    arreglos[i]=arregloGuardador#Arreglo es el arreglo que contiene arreglos

#for i in range(0,len(arreglos),1):
    #print(arreglos[i])


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

def promedio(matriz):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            suma = matriz[i][j]+suma
    return suma/(len(matriz)*len(matriz[0]))

#def aLaMierdaNoSeHacerlo(matriz):


for i in range(0,len(rangosALeer),1):
    for j in range(0,len(arreglos),1):

        Lista1 = arreglos[i]
        Lista2 = arreglos[j]

        Arreglo1, Arreglo2 = mergesort(Lista1, Lista2)# Ordenar Lista1 y reordenar Lista2 según el orden de Lista1

        #print(f"Estudiante {i+1} ordenada: {Arreglo1} Estudiante {j+1} ordenada: {Arreglo2}")

print(f"El promedio es: {promedio(arreglos)}")




