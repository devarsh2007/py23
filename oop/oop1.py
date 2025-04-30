# creating class 
class person:
    def __init__(self):
        print("constructor called....")
    
    def walk(self):
        print("i can walk")
        
    def talk(self):
        print("i can talk")

# creating class obj
p1 = person()
p1.walk()
p1.talk()

p2 = person()
p2.walk()
p2.talk()

p3=person()