#find greatest & smallest

L=[12,60,6,88,23,56,45,2,91]
largest=smallest=L[1]
for i in range(0,len(L)):
    if(largest<L[i]):
       largest=L[i]
    elif(smallest>L[i]):
        smallest=L[i]
        
print("Smallest no. ",smallest,"\nGreatest no. ",largest)
