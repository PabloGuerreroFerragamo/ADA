def fibo(n,kuromi):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(kuromi[n]!=None):
        return kuromi[n]
    else:
        kuromi[n]=fibo(n-1,kuromi)+fibo(n-2,kuromi)
    return kuromi[n]

numero=7
arreglo=[None]*(numero+1)
print(fibo(numero,arreglo))