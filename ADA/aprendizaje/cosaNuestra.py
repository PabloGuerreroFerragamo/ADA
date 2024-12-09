def corteDeVarilla(longitud,memory,precios):
    if longitud==0:
        return 0

    if(memory[longitud]!=-1):
        return memory[longitud],[]

    precioMax=0
    mejoresCortes=[]

    for corte in range(1,longitud+1):
        precioActual=precios[corte-1]
        precioRestante,cortesRestantes=corteDeVarilla(longitud-corte,memory,precios)
        precioTotal=precioActual+precioRestante

        if(precioTotal>precioMax):
            precioMax=precioTotal
            mejoresCortes = [corte] + cortesRestantes

    memory[longitud] = precioMax
    return precioMax, mejoresCortes


long = 4
memory = [-1] * (long + 1)
precio=[1,3,5,8]

precioMaximo, cortesOptimos = corteDeVarilla(long, memory, precio)
print(f"precio maximo es: {precioMaximo}")
print(f"Los cortes son: {cortesOptimos}")