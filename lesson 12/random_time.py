import random
import time
def getrandomdate(startdate,enddate):
    print(f"printing random day between {startdate} and {enddate}")
    randomgenarator=random.random()
    dateformat="%d/%m/%Y"
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+randomgenarator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print(f"the random date is {getrandomdate("1/9/2024","4/6/2080")}")