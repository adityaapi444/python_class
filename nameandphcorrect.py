name=input("enter your name")
ph=(input("enter phone no.(w/o country code)"))
if(len(name)>2 and name.isalpha() and len(name)<=25 and len(ph)==10 and  ph.isdigit()):
    print("name={}\nphone no={}".format(name,ph))
else:
    print("Incorrect Details")
