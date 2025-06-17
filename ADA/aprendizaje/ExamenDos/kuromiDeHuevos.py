def elKuromi(pesoMax,beneficio,pesoObjeto,Vop):
    for objeto in range(1,len(beneficio)+1,1):
        for pesoActual in range(0,pesoMax+1,1):
            if(pesoObjeto[objeto-1]<=pesoActual):
                Vop[objeto][pesoActual]=max(beneficio[objeto-1]+Vop[objeto-1][pesoActual-pesoObjeto[objeto-1]],Vop[objeto-1][pesoActual])
            if(pesoObjeto[objeto-1]>pesoActual):
                Vop[objeto][pesoActual]=Vop[objeto-1][pesoActual]

def rastrear_elementos(pesoMax, pesoObjeto, beneficio, Vop):
    elementos_incluidos = []
    pesoActual = pesoMax
    for objeto in range(len(beneficio), 0, -1):
        # Si el valor cambia al moverse hacia arriba, el objeto fue incluido
        if Vop[objeto][pesoActual] != Vop[objeto-1][pesoActual]:
            elementos_incluidos.append(objeto-1)  # Guardar el índice del objeto
            pesoActual -= pesoObjeto[objeto-1]  # Reducir el peso restante
    return elementos_incluidos

pesoMax=5
beneficio=[30,15,20]
peso=[3,2,1]
matriz=[[0]*(pesoMax+1) for _ in range(0,len(peso)+1,1)]

elKuromi(pesoMax,beneficio,peso,matriz)

arreglo=rastrear_elementos(pesoMax,peso,beneficio,matriz)

print("Beneficio de los objetos incluidos")

for i in range(0,len(arreglo),1):
    print(beneficio[arreglo[i]])