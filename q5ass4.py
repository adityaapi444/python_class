#fibonacci
l=[]
n=int(input("enter no.of terms"))
for i in range(0,n):
    if(i<=1):
        l.append(i)
    else:
        l.append(l[i-2]+l[i-1])
print(l)

