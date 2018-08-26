L=['Apple','Mango',2,4.5,6,2,'Apple',4.5,2,'Apple']
L_uni=[]
for each in L:
    if each not in L_uni:
        L_uni.append(each)
        print(each,L.count(each))
