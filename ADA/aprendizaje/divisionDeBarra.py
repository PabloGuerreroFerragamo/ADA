def corteDeVarilla(longitud,memory,precios):
    precioMax=0
    guardador=0
    cortador=0
    if(longitud==0):
        return 0

    if(memory[longitud]!=-1):
        return memory[longitud]

    for corte in range(1,longitud+1,1):#incluimos la longitud completa de la varilla, ya que range en 4 llega hasta 3
        if(precioMax>precios[corte-1]+corteDeVarilla((longitud-corte),memory,precios)):
            precioMax=precios[corte-1]+corteDeVarilla((longitud-corte),memory,precios)

    memory[longitud]=precioMax
    return precioMax

long=4
memory=[-1]*(long+1)

precio=[1,5,8,9]

print(f"El precio es: {corteDeVarilla(long,memory,precio)}")

