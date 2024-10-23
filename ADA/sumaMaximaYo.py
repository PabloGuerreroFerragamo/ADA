def sumaMaxima(Datos):
    if (len(Datos) > 1):
        DatosI = Datos[0:len(Datos) // 2]
        DatosD = Datos[len(Datos) // 2:]

        sumaMaxI = -10000
        sumaMaxD = -10000
        sumaI = 0
        sumaD = 0

        for i in range(0, len(DatosI), 1):
            sumaI = DatosI[len(DatosI) - 1 - i] + sumaI
            if (sumaI > sumaMaxI):
                sumaMaxI = sumaI

        for j in range(0, len(DatosD), 1):
            sumaD = DatosD[j] + sumaD
            if (sumaD > sumaMaxD):
                sumaMaxD = sumaD

        return sumaMaxI + sumaMaxD


arreglo = [1, 2, 3, 4, 5, 6]
print(sumaMaxima(arreglo))