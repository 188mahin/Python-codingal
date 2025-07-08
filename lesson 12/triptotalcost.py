def hotel_cost(days):
    return 1100*days
def plane_ride_cost(city):
    if city.lower()=='london':
        return 11450
    elif city.lower()=='rio de janiero':
        return 29340
    elif city.lower()=='cairo':
        return 6780
    elif city.lower()=='new york':
        return 33490
def car_cost(days):
    if days>=7:
        return 120*days - 200
    elif days>=3:
        return 130*days - 100
    else:
        return 140*days
def trip_cost(city,days,spendingmoney,tax):
    return car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spendingmoney+tax
d=int(input("enter the number of days you want to stay there"))
c=(input("enter the city from (new york,rio de janiero,cairo,london)"))
spendingmoney=int(input("enter the amount of money you can spend in that city"))
print(f"the cost of your car rental is {car_cost(d)}")
print(f"the cost of your plane ride is {plane_ride_cost(c)}")
print(f"the cost of your hotel is {hotel_cost(d)}")
print(f"the total trip cost is {trip_cost(c,d,spendingmoney,6730)}")