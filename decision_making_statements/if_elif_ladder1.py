# calculator

# 1->addition
# 2->subtraction
# 3->multiplication
# 4->division

print("""
# 1->addition
# 2->subtraction
# 3->multiplication
# 4->division""")

choise = int(input("enter your choise : "))

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

if choise==1:
    print(f"addition : {a+b}")
    
elif choise==2:
    print(f"subtraction : {a-b}")
    
elif choise==3:
    print(f"multiplication : {a*b}")
    
elif choise==4:
    print(f"division : {a/b}")
        
else:
    print('Invalid input!!!')
