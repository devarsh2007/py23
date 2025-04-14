try:
    file = open("../exercise.txt")
    
except:
    print("give correct file name")

else:
    print(file.read())
    file.close()


