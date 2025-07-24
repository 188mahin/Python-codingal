class IOString:
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("enter the string:")
    def print_string(self):
        print("The string is:",self.str1.upper())
str1=IOString()
str1.get_string()
str1.print_string()