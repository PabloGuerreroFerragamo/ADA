import random

def corteDeVarilla(longitud,memory,precios):
    precioMax=0
    if(longitud==0):
        return 0

    if(memory[longitud]!=-1):
        return memory[longitud]

    for corte in range(1,longitud+1,1):#incluimos la longitud completa de la varilla
        precioMax=max(precioMax,precios[corte-1]+corteDeVarilla((longitud-corte),memory,precios))#El -1 es por el indice 0 del arreglo

    memory[longitud]=precioMax
    return precioMax

long=4
memory=[-1]*(long+1)


precio=[1,3,5,8]

# Genera un número aleatorio que será la cantidad de posiciones en la lista
cantidad_elementos = random.randint(1, long)
print(f"Cantidad de elementos a generar: {cantidad_elementos}")

# Genera una lista con 'cantidad_elementos' números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(cantidad_elementos)]
print(numeros_aleatorios)


print(f"Hola Pana, el precio es: {corteDeVarilla(long,memory,numeros_aleatorios)}")#metele precios que es el del profe

