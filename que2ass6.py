d1={'Python':3,'Java':6,'Perl':2}
d2={'C++':5,'angularJS':3,'Python':5}
d=dict(d1)  
d.update(d2)
for k in d2:
    if k in d1.keys():
        d[k]=d1[k]+d2[k] 
print("d1:",d1,"\nd2 :",d2,"\nd :",d)

