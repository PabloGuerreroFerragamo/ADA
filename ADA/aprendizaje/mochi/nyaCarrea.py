def valorOptimo(beneficio,pesoObjeto,pesoMax,Vop):
    for pesoActual in range(0,pesoMax+1,1):
        for objeto in range(0,len(pesoObjeto),1):
            if(pesoActual!=0 or objeto!=0):
                if (pesoObjeto[objeto] <= pesoActual):
                    if(objeto>0):
                        Vop[pesoActual][objeto] = max(beneficio[objeto] + Vop[objeto - 1][pesoActual - pesoObjeto[objeto]],Vop[objeto - 1][pesoActual])
                    else:
                        Vop[pesoActual][objeto]=beneficio[objeto]
                if (pesoObjeto[objeto] > pesoActual):
                    if (objeto > 0):
                        Vop[pesoActual][objeto] = Vop[objeto - 1][pesoActual]
                    else:
                        Vop[pesoActual][objeto] = beneficio[objeto]

pesoMax=5
beneficio=[10,20,30]
peso=[2,1,4]
matriz=[[0]*(pesoMax+1) for _ in range(0,len(peso)+1,1)]

for fila in matriz:
    print(fila)

valorOptimo(beneficio,peso,pesoMax,matriz)

print("Matriz final")

for fila in matriz:
    print(fila)