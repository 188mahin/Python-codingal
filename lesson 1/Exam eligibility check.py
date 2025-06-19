medical_cause=str(input("Do you have a medical cause. Please write your input in a capital Y or N:"))
attendence=int(input("what is your attendence:"))
if medical_cause=='Y':
    print("you are allowed")
else:
    if attendence>=75:
        print("you are allowed")
    else:
        print("you are not allowed")
   