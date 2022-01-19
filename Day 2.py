#mutable -List , dict, set
# immutable - int, float, boolean, str, tuple

a = 10
print(id(a))
a = "tech"
print(id(a))

l = [1,3,4]
print(l)
print(id(a))
l.append(10)
print(l)
print(id(a))

name = input ("Enter your name : ")
age = input ("Enter your age : ")
occ = input("What are you doing : ")

print("Hi my name is " +name)
print( "I am " +age,"years old")
print("and " +occ)