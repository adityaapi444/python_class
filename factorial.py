num=int(input("enter a number\t"))
fact=1

for i in range(num,0,-1):
    fact=fact*i
print("{}!= {}".format(num,fact))
    
