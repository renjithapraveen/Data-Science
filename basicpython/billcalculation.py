def billcalc(billamount,tiperc):
    total = billamount+(1+0.01*tiperc)
    print("total amount =$",total)
billamount=float(input("enter the bill amount:"))
tiperc=float(input("enter the tip percentage:"))
billcalc(billamount,tiperc)