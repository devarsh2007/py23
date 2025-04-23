        # 1
    # 1   2   1
#1    2   3   2    1 

l=0
for m in range(1,4):
    row = 3
    for i in range(1,row-l):
        print(" ",end=" ")
        
    for j in range(1,row-i+m):   
        print(j,end=" ")
        
    for k in range(j-1,0,-1):
        print(k,end=" ")

    print()
    l+=1

# row=3 
# for i in range(1,row-1):
#     print(" ",end=" ")
    
# for j in range(1,row-i+1):
#     print(j,end=" ")
    
# for k in range(j-1,0,-1):
#     print(k,end=" ")
# print()

# row=3
# for i in range(1,row-2):  
#     print(" ",end=" ")
    
# for j in range(1,row-i+2):
#     print(j,end=" ")

# for k in range(j-1,0,-1):
#     print(k,end=" ") 
# print()