L=['Mango','Grapes','Mango','Apple','Grapes','Grapes']
L1=(list(set(L)))
L1.sort()
word_list=[]
count_list=[]
for each in L1:
    word_list.append(each)
    count_list.append(L.count(each))
print("word_list = ",word_list,"\ncount_list = [",count_list)
