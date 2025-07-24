class sum:
    def twosum(self,nums,target):
        lookup={}
        for i,num in enumerate(nums):
            if target- num in lookup:
                return(lookup[target-num],i)
            lookup[num]=i
value=int(input("enter the sum of two numbers that you want search:"))
print("index1=%d ,index2=%d" %sum().twosum((10,4,20,2,30,3,40,5),value))

        