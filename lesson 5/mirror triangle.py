n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
        
    for k in range(n-(i+1),0,-1):
        print(" ",end=" ")
        
    for k in range(n-(i+1),0,-1):
        print(" ",end=" ")
        
    for j in range(i+1):
            print("*",end=" ")
            
    print()

    

        
       
        
        
        
    
    
    
    
    
    
    
