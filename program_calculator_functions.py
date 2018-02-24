#program for calculator using function
x=int(input("enter the x value:"))
y=int(input("enterthe y value:"))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
print(add(x,y))
print(sub(x,y))
print(mul(x,y))
print(div(x,y))
print(mod(x,y))
