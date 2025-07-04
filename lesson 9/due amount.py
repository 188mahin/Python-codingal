def due():
    return round(bill_amount-payed,2)
bill_amount=float(input("enter the bill amount:"))
payed=float(input("enter the amount payed:"))
print(f"the amount due by the customer is {due()}")