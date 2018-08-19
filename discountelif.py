MRP=float(input("enter the price\t"))
offer=int(input("select any one offer\n1. 75%\n2. 60%\n3. 40%\t"))
if(offer==1):
    MRP=MRP-MRP*0.75
    print("To Pay : {}".format(MRP))
elif(offer==2):
    MRP=MRP-MRP*0.6
    print("To Pay : {}".format(MRP))
elif(offer==3):
    MRP=MRP-MRP*0.4
    print("To Pay : {}".format(MRP))
else:
    print("To Pay : {}".format(MRP))
