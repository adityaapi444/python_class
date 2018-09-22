class employee:
    'This is a class of employee.class employee is parent of class manager and developer'
    def __init__(self,eid,name,age):
        self.e_id=eid
        self.name=name
        self.age=age
    def display(self):
        print('E_id :',self.e_id,'E_name :',self.name,'E_age :',self.age,'prof :',self.designation)
    def __add__(self,m):
        max1=self.sal
        for i in range(len(m)):
            if max1<=m[i].sal:
                max1=m[i].sal
                z=i
        print('manager having highest salary')
        print('e_id :',m[z].e_id,'name :',m[z].name,'age :',m[z].age,'salary :',m[z].sal)
    def __mul__(self,m):
        min1=self.sal
        for i in range(len(m)):
            if min1>=m[i].sal:
                min1=m[i].sal
                w=i
        print('develoer having lowest salary')
        print('e_id :',m[w].e_id,'name :',m[w].name,'age :',m[w].age,'salary :',m[w].sal)

class manager(employee):
    def __init__(self,sal,a,b,c):
        self.designation="manager"
        self.sal=sal
        employee.__init__(self,a,b,c)
class developer(employee):
    def __init__(self,sal,a,b,c):
        self.sal=sal
        self.designation="developer"
        employee.__init__(self,a,b,c)
m=[]
d=[]
print (employee.__doc__)
print("enter details for 5 manager")
for i in range (5):
    a=input("enter e_id")
    b=input("enter emp name")
    sal=float(input("enter salary"))
    c=int(input("enter age"))
    m.append(manager(sal,a,b,c))
    
print("enter details for 5 developer")
for i in range (5):
    a=input("enter e_id")
    b=input("enter emp name")
    sal=float(input("enter salary"))
    c=int(input("enter age"))
    d.append(developer(sal,a,b,c))
for i in range(len(m)):
    m[i].display()
for i in range(len(m)):
    d[i].display()
#operator overloading
m[0]+(m)
d[0]*(d)




