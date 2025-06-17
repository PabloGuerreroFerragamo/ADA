from multiprocessing import Pool
import time
import math
import random
import numpy as np


def merch(lista, listaIzq, listaDer):
    i = 0
    j = 0
    k = 0
    while i < len(listaIzq) and j < len(listaDer):
        if (listaIzq[i] < listaDer[j]):
            lista[k] = listaIzq[i]
            i = i + 1
            k = k + 1
        else:
            lista[k] = listaDer[j]
            j = j + 1
            k = k + 1
    while i < len(listaIzq):
        lista[k] = listaIzq[i]
        i = i + 1
        k = k + 1
    while j < len(listaDer):
        lista[k] = listaDer[j]
        j = j + 1
        k = k + 1


def melchor(lista):
    n=len(lista)
    mita = n // 2  # las // significan division entera padrinoli
    listaIzq = lista[:mita]
    listaDer = lista[mita:]

    for i in range(0, mita, 1):
        listaIzq[i] = lista[i]

    for i in range(mita, n, 1):
        listaDer[i - mita] = lista[i]

    if (n > 1):
        melchor(listaIzq)
        melchor(listaDer)
        merch(lista, listaIzq, listaDer)


def parallel_mergesort(Datos):
    if len(Datos) <= 1:
        return Datos

    n = len(Datos)

    cuarto = n // 4

    mitad=n//2

    listaUno = Datos[0:cuarto]
    listaDos = Datos[cuarto:(cuarto*2)]
    listaTres = Datos[(cuarto*2):(cuarto*3)]
    listaCuatro = Datos[(cuarto*3):n]

    if __name__ == '__main__':

        with Pool(4) as p:
            p.map(melchor,[listaUno,listaDos,listaTres,listaCuatro])

        primerLista=Datos[:mitad]
        segundaLista=Datos[mitad:]

        listaFinal=Datos[:n]

        merch(primerLista,listaUno,listaDos)
        merch(segundaLista, listaTres,listaCuatro)
        merch(listaFinal,primerLista,segundaLista)

    return Datos

if __name__ == '__main__':
    Datos = np.random.permutation(3000000)
    start_time = time.perf_counter()
    sorted_Datos= parallel_mergesort(Datos)
    #print(sorted_Datos)
    finish_time = time.perf_counter()
    print("Tiempo de ejecución multiprocessing: {}".format(finish_time - start_time))

    start_time=time.perf_counter()
    sorted_Datos=melchor(Datos)
    #print(sorted_Datos)
    finish_time=time.perf_counter()
    print("Tiempo de ejecución en serie: {}".format(finish_time - start_time))