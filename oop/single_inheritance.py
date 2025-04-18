# single level inheritance
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def walk(self):
        print("i can walk")
        
    def talk(self):
        print("i can talk")  
        
class student(person):
    def __init__(self, name, age,id,school):
        super().__init__(name, age)
        self.id=id
        self.school = school
    
    def write(self):
        print("i can write")
        
    def read(self):
        print("i can read")
        
    def studentdetails(self):
        print(self.name)    
        print(self.age) 
        print(self.id) 
        print(self.school) 
        
s1 = student("devarsh",12,121,"sp")
s1.write()
s1.read()
s1.walk()
s1.talk()
s1.studentdetails()