file = open("demo.txt","r")
# print(file)

for i in file:
    for j in i:
        print(j,end="")
    
file.close()