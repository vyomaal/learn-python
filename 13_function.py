#function without argument
def add():
    print("i am executed")
    return 1+2

#print(add())
#print(add(2)) #it will give error

#function with argument
def add(a,b):
    return a+b

#print(add(5,6))

#default argument
def add(a=10,b=12):
    return a+b
print(add())

#args
def arguments(*args):
    print("from argument function.", type(args))
    print(args)
    return sum(args)
print (arguments(4,5,6))

def arguments(one, two, *args): 
    print("from argument function.", type(args))
    print(args)
    return sum(args)
print (arguments(4,5,6))

#kwargs
def keyarguments(name ,**kwargs):
    print("from key function.", type(kwargs))
    print(kwargs)
    return kwargs
print (keyarguments(name = "iims", day = "monday"))