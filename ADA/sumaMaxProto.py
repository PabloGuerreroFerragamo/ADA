def sumaMaxima(Datos):
    if len(Datos) == 1:
        return (Datos[0], Datos)

    # Divide el arreglo en dos mitades
    mit = len(Datos) // 2
    DatosI = Datos[:mit]
    DatosD = Datos[mit:]

    # Suma máxima del lado izquierdo
    SumaMaxI, subArrayI = sumaMaxima(DatosI)

    # Suma máxima del lado derecho
    SumaMaxD, subArrayD = sumaMaxima(DatosD)

    # Suma máxima cruzada entre las dos mitades
    sumaI = 0
    sumaCumI = -float('inf')
    DatosCumI = []

    for i in range(mit - 1, -1, -1):
        sumaI += Datos[i]
        if sumaI > sumaCumI:
            sumaCumI = sumaI
            DatosCumI = Datos[i:mit]

    sumaD = 0
    sumaCumD = -float('inf')
    DatosCumD = []

    for j in range(mit, len(Datos)):
        sumaD += Datos[j]
        if sumaD > sumaCumD:
            sumaCumD = sumaD
            DatosCumD = Datos[mit:j + 1]

    # Suma cruzada
    SumaC = sumaCumI + sumaCumD
    DatosC = DatosCumI + DatosCumD

    # Devuelve la suma máxima entre las tres opciones: izquierda, derecha, cruzada
    if SumaMaxI >= SumaMaxD and SumaMaxI >= SumaC:
        return (SumaMaxI, subArrayI)
    elif SumaMaxD >= SumaMaxI and SumaMaxD >= SumaC:
        return (SumaMaxD, subArrayD)
    else:
        return (SumaC, DatosC)


# Ejemplo
arreglo = [-1, -2, -13, 4, 5, 6]
print(sumaMaxima(arreglo))
