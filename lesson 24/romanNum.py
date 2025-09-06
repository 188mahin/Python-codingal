class IntegertoRoman:
    def __init__(self):
        self.value_symbol_pairs=[
            (1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
            (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
            (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")
            ]
    def converter(self,num:int)->str:
        roman=[]
        for i,(value,symbols) in enumerate(self.value_symbol_pairs):
            count=0
            while num>=value:
                roman.append(symbols)
                num-=value
                count+=1
        return "".join(roman)

romNum=int(input("enter a integer:"))
convert=IntegertoRoman()
print(convert.converter(romNum))
