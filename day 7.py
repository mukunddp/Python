# functions

# block of organized and resuble code

#def function():
    #Statements 1
   # Statements 2
    #Statements 3

#argument and parameters

def printTable(num):
    for i in range (1,11):
        print(i*num)


printTable(10)

def add(a,b):
    c  = a + b
    print(c)

add(4,15)

def add3(a,b,z=5):
    c  = a + b +z
    print(c)
    return c # always give data to function who called it.


print(add3(4, 15, 4))
print(add3(5,40))
