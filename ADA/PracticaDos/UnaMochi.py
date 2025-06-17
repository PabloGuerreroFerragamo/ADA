def valorOptimo(beneficio,peso,pesoMax,Vop):
    for i in range(0,pesoMax+1,1):
        for j in range(0,len(peso),1):
            if(i==0 or j==0):
                Vop[i][j]=0
            else:
                if (peso[j] <= i):  # el objeto entra
                    Vop[j][i] = max(beneficio[j] + Vop[j - 1][i - peso[j]], Vop[j - 1][i])

                if (peso[j] > i):
                    Vop[j][i] = Vop[j - 1][i]

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