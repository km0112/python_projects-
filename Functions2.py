def feedme ():
    x = int(input ("Feed me a number"))
    return x

def out (x):
    print("my answer", x)

x = feedme()
out(x)
y = feedme()
out(y)

def subtract(x,y):
    print(x-y)

def add(x,y):
    print(x+y)

def multiply(x,y):
    print(x*y)

def divide(x,y):
    print(x/y)

"""def exp(x,y):
    print(x^y)"""
Answer=input("would you like to run this program?")

if "y" in Answer:
    multiply(x,y)
    divide(x,y)
    add(x,y)
    subtract(x,y)
    r=input("Would you like to go again?")
    break if "no" in r


"""exp(x,y)

def exp_rev(x,y):
    print(x^y)"""



# user input
