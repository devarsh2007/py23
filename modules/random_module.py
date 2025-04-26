from random import *

print(random())  #0.0 - 1.0

# give random float value between range
print(uniform(2 , 10))  

# give random int value between range
print(randint(1,100))

# give random int value between range with gap
print(randrange(1,100,10))

l1 = ['a','b','c','d']
print(choice(l1)) 

t1 = ('red','blue','green','yellow','black')
print(choice(t1))