class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + "("+ self.meaning + ")"
flash=[]
print("welcome to flash card application")
while True:
    word=input("enter the word you want to keep in your flashcard:")
    meaning=input("enter the meaning for the word:")
    flash.append(flashcard(word,meaning))
    option=int(input("enter 0 to continue else type 1:"))
    if (option):
        break
print("your flashcards are:")
for i in flash:
    print(">",i)