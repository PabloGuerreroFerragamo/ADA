def sumaMaxima(Datos):
    if(len(Datos)>1):
        mit=len(Datos)//2
        SumaMaxI=-10000
        DatosI=(Datos[:mit])
        SumaMaxD=-10000
        DatosD=(Datos[mit:])

        sumaI=0
        sumaCumI=-10000
        for i in range(mit-1,-1,-1):
            sumaI=sumaI+DatosI[i]
            if(sumaI>sumaCumI):
                sumaCumI=sumaI
                DatosCumI=DatosI[i:mit]

        suma=0
        sumaCumD=-100000
        for j in range(0,len(DatosD),1):
            suma=suma+DatosD[j]
            if(suma>sumaCumD):
                sumaCumD=suma
                DatosCumD=DatosD[0:j+1]

        SumaC=sumaCumI+sumaCumD
        DatosC=[DatosCumI,DatosCumD]

        #Suma maxima

        if(SumaMaxI>SumaMaxD and SumaMaxI>SumaC):
            return (SumaMaxI,DatosI)
        elif(SumaMaxD>SumaMaxI and SumaMaxD>SumaC):
            return (SumaMaxD,DatosD)
        else:
            return (SumaC,DatosC)
    else:
        return (Datos,Datos)

arreglo = [-1, -2, -13, 4, 5, 6]
print(sumaMaxima(arreglo))