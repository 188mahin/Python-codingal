theBoard={'7':' ', '8':' ', '9':' ',
          '4':' ', '5':' ', '6':' ',
          '1':' ', '2':' ', '3':' '}
Board_keys=[]
for key in theBoard:
    Board_keys.append(key)
def printBoard(Board):
    print(Board['7']+ '|'+ Board['8']+ '|'+Board['9'])
    print('-+-+-')
    print(Board['4']+ '|'+ Board['5']+ '|'+Board['6'])
    print('-+-+-')
    print(Board['1']+ '|'+ Board['2']+ '|'+Board['3'])
def game():
    turn='X'
    count=0
    for i in range(10):
        printBoard(theBoard)
        print(f"Its your turn,{turn}.Where do you want to move")
        move=input()
        if theBoard[move]==' ':
            theBoard[move]=turn
            count+=1
        else:
            print("this place has been filled. Move to a different place ")
            continue
        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
            elif theBoard['1']==theBoard['4']==theBoard['7']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
            elif theBoard['2']==theBoard['5']==theBoard['8']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
            elif theBoard['3']==theBoard['6']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
            elif theBoard['7']==theBoard['5']==theBoard['3']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
            elif theBoard['1']==theBoard['5']==theBoard['9']!=' ':
                printBoard(theBoard)
                print("game over")
                print(turn," wins")
                break
        if count==9:
            print("game over its a tie")
        if turn=='X':
            turn='O'
        else:
            turn='X'
    restart=input("Do you want to play again (y/n)")
    if restart.lower()=='y':
        for key in Board_keys:
            theBoard[key]=' '
        game()
    
        
if __name__=="__main__":
    game()
    


