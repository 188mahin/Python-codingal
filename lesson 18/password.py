import random
def password(length=9):
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    rand= ''.join(random.choice(chars) for _ in range(length))
    return rand
if __name__=="__main__":
    while True:
        print('random password is',password())
        n=input("do want to generate another password(y/n)").strip().lower( )
        if n!='y':
            break
