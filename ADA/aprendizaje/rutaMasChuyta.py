def muchosMapas(matriz,cambioDeCiudad):
    valorMinimo=9999999999
    suma=0
    if(cambioDeCiudad==len(matriz)-1):
        return 0

    for i in range(0,len(matriz[cambioDeCiudad]),1):
        if(matriz[cambioDeCiudad][i]!=-1):
            suma=matriz[cambioDeCiudad][i]+muchosMapas(matriz,i)
            valorMinimo=min(valorMinimo,suma)
    return valorMinimo

ciudades=10
avance=0
mapa=[[-1]*ciudades for _ in range(0,ciudades,1)]

mapa[0][1]=2
mapa[0][2]=4
mapa[0][3]=3


mapa[1][4]=7
mapa[1][5]=4
mapa[1][6]=6

mapa[2][4]=3
mapa[2][5]=2
mapa[2][6]=4

mapa[3][4]=4
mapa[3][5]=1
mapa[3][6]=5


mapa[4][7]=1
mapa[4][8]=4

mapa[5][7]=6
mapa[5][8]=3

mapa[6][7]=3
mapa[6][8]=3


mapa[7][9]=3

mapa[8][9]=4

ciudade=0
print(muchosMapas(mapa,ciudade))