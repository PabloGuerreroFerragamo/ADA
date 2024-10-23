def maxMin(Datos):
    if(len(Datos)>1):
        DatosI=Datos[0:len(Datos)//2]
        DatosD=Datos[len(Datos)//2:]

        maxI,minI=maxMin(DatosI)
        maxD,minD=maxMin(DatosD)

        if(maxD>maxI):
            maximo=maxD
        else:
            maximo=maxI

        if(minD<minI):
            minimo=minD
        else:
            minimo=minI

        return maximo,minimo
    else:
        maximo=Datos[0]
        minimo=Datos[0]
        return maximo,minimo

arreglo=[4,2,5,8,1]
print(maxMin(arreglo))