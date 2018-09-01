s=input("enter a string")
l=s.split()
max=0
for each in l:
    if len(each)>max:
        max=len(each)
for each in l:
    if len(each)==max:
        print(each)
    
