def valorOptimo(beneficio,peso,pesoMax,):
    for i in range(0,pesoMax+1,1):
        for j in range(0,len(peso)+1,1):
            if(peso[j]<=i):



pesoMax=5
beneficio=[10,20,30]
peso=[2,1,4]
matriz=[[0]*(pesoMax+1) for _ in range(0,len(peso)+1,1)]

print(matriz)