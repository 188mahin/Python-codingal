import random
options=["rock","paper","scissors"]

playing=True
while playing:
    user_choice=input("enter rock,paper or scissors - type 'exit' to quit:")
    if user_choice.lower()=='exit':
        print("thanks for playing")
        break
    comp_choice=random.choice(options)
    if user_choice==comp_choice:
        print("It is a tie!")
    elif user_choice=='rock' and comp_choice=='scissors':
        print("you win! Rock crushes the scissors")
    elif user_choice=='paper' and comp_choice=='rock':
        print("You win! Paper covers the rock")
    elif user_choice=='scissors' and comp_choice=='paper':
        print("You win! scissors cuts through the paper")
    else:
        print("You lose")
    