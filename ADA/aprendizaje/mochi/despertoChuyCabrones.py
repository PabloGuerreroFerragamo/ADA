def valorOptimo(beneficio,pesoObjeto,pesoMax,Vop):
    for objeto in range(0, len(pesoObjeto), 1):
        for pesoActual in range(0,pesoMax+2,1):

            if(objeto==0):
                print(f"Peso actual={pesoActual} y objeto{objeto}")
                Vop[pesoActual][objeto]=0

            elif(pesoActual==0):
                Vop[pesoActual][objeto]=0

            else:

                if (pesoObjeto[objeto] <= pesoActual):
                        Vop[pesoActual][objeto] = max(beneficio[objeto] + Vop[objeto - 1][pesoActual - pesoObjeto[objeto]],Vop[objeto - 1][pesoActual])

                if (pesoObjeto[objeto] > pesoActual):
                        Vop[pesoActual][objeto] = Vop[objeto - 1][pesoActual]

        print("Hola Chuy")
        for fila in matriz:
            print(fila)


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