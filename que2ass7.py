def emi_calc(p,n,r):
    n=n*12
    r=r/(12*100)
    m=(1+r)**n
    return (p*r*m)/(m-1)
pr=int(input("Enter priciple amt."))
t=int(input("enter no.of years"))
ri=float(input("enter rate of Interest"))
print("EMI = ",round(emi_calc(pr,t,ri),2))
