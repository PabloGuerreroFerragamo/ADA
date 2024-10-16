box=[5,4,3,1,9]
aux=0
a=len(box)

for n in range(0,a-1,1):#empezamos desde cero, ya que como son arreglos pues xd
    for m in range(0,a-1-n,1):#No debe llegar al final, por que ya se cual es el mayor
        if(box[m]>box[m+1]):#intercambias trolo
            aux=box[m]
            box[m]=box[m+1]
            box[m+1]=aux
print(box)
