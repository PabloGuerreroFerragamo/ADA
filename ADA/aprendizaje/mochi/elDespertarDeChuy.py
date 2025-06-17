def corteDeVarilla(longitud,memory,precios):
    precioMax=0

    if(longitud==0):
        return 0

    if(memory[longitud]!=-1):
        return memory[longitud]

    for corte in range(1,longitud+1,1):#incluimos la longitud completa de la varilla, ya que el range solo
        precioMax=max(precioMax,precios[corte-1]+corteDeVarilla((longitud-corte),memory,precios))#El -1 es por el indice 0 del arreglo
    memory[longitud]=precioMax
    return precioMax

long=4
memory=[-1]*(long+1)
precio=[1,3,5,8]

print(f"Hola chuy, el precio es: {corteDeVarilla(long,memory,precio)}")#metele precios que es el del profe