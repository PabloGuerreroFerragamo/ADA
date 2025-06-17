Nnodos=8
nodos={'A':[('B',1),('C',4)],
       'B':[('A',1),('C',3),('D',3),('E',5)],
       'C':[('A',4),('B',3),('E',3),('F',1)],
       'D':[('B',3),('E',1),('G',2)],
       'E':[('B',5),('C',3),('D',1),('F',1)],
       'F':[('C',1),('E',1),('H',3)],
       'G':[('D',2),('H',1)],
       'H':[('G',1)]}

infinito=float('inf')

dist={'A':0,'B':infinito,'C':infinito,'D':infinito,'E':infinito,'F':infinito,'G':infinito,'H':infinito}

predecesor={'A':'A','B':'B','C':'C','D':'D','E':'E','F':'F','G':'G','H':'H'}

Nnovisitados=['A','B','C','D','E','F','G','H']

posicion='A'
final='H'


#mientras existan elementos en Nnovisitados
while Nnovisitados:
    # inicializar el vecino de costo mínimo
    