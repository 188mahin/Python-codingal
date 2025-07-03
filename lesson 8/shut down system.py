import os
def shutdown():
    user=input("do you want to shut down your computer (yes/no)")
    if user=='yes':
        os.system("shutdown /s /t 1")
    else:
        print("shutdown cancelled")
shutdown()