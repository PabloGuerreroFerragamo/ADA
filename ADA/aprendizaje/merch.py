def merch(lista, listaIzq, listaDer):
    i=0
    j=0
    k=0
    while i<len(listaIzq) and j<len(listaDer):
        if(listaIzq[i]<listaDer[j]):
            lista[k]=listaIzq[i]
            i=i+1
            k=k+1
        else:
            lista[k]=listaDer[j]
            j=j+1
            k=k+1
    while i<len(listaIzq):

        lista[k]=listaIzq[i]
        i=i+1
        k=k+1
    while j<len(listaDer):

        lista[k]=listaDer[j]
        j=j+1
        k=k+1

def melchor(lista, n):
    mita=n//2#las // significan division entera padrinoli
    listaIzq=[i for i in range(0,mita,1)]
    listaDer=[i for i in range(0,mita,1)]

    for i in range(0,mita,1):
        listaIzq[i]=lista[i]

    for i in range(mita,n,1):
        listaDer[i]=lista[i]

    if(n>1):
        melchor(listaIzq,mita)
        melchor(listaDer,n-mita)
        merch(lista,listaIzq,listaDer)

box=[4,3,5,7,8,9,1,2]
melchor(box,len(box))
print(box)