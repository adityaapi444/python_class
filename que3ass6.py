d={'Python': 8, 'Java': 6, 'Perl': 2, 'C++': 5, 'angularJS': 3,'Ruby':9,'Bootstrap':1}
l=[]
def asd():
    for k,v in d.items():
        g=max(d.values())
        if d[k]==g:
            l.append(k)
            d.pop(k)
            break
for k in range(len(d)):
    if k!=0 :
        asd()
        
print(l[0:3])
