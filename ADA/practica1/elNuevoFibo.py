def fibo(n,kuromi):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        kuromi[0]=0
        kuromi[1]=1
        for i in range(2,n+1,1):
            kuromi[i]=kuromi[i-1]+kuromi[i-2]

        return kuromi[n]


numero=7
arreglo=[None]*(numero+1)
print(fibo(numero,arreglo))
