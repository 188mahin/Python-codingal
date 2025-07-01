def tip(x,y):
    total=x*(1+0.01*y)
    total=round(total,2)
    print(f"your total is {total}")
bill_amount=float(input("enter the bill amount"))
tip_perc=float(input("enter the tip percentage"))
tip(bill_amount,tip_perc)