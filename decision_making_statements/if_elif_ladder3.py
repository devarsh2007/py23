# Grade Calculator

# Take marks as input and assign grades based on the following:
# 90+ → A
# 80-89 → B
# 70-79 → C
# 60-69 → D
# Below 60 → F

# 3 subject mrks
maths = int(input("enter maths marks : "))
science = int(input("enter science marks : "))
eng = int(input("enter english marks : "))

if (maths<0 or maths>100) or (eng<0 or eng>100) or (science<0 or science>100): 
    print("wrong")

# persantage
marks = (maths+eng+science) / 3
print(round(marks,2))

marks = round(marks,2)