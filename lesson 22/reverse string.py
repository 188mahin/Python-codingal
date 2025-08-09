class reverseString:
    def reverse(self):
        __string=input("enter a word:")
        string2=""
        for i in __string:
            string2=i+string2
        print("reversed string",string2)
obj=reverseString()