import random

print(type("Ranjeet"))
print(type(2))
print(type(2.0))

#Type Conversion
print(int("123")+int("231"))

print(6/3)# will return float
print(5/3) # will return with decimal
print(5//3) # will return the floor value

#f String
name = "Ranjeet"
age = 26
print(f"My name is {name} and I am {age} year old")#F String uses

print(10 % 3)    # Output: 1
print(-10 % 3)   # Output: 2
print(10 % -3)   # Output: -2 takes the sign of the divisor.


#random imported at the beginning
inta = random.randint(1,20)
print(inta)