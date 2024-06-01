import math

# author Kaila McNamara

#input 2 numbers
a=float(input("1st number \n"))
b=float(input("2nd number \n"))

print("1st number is " +str(a))
print("2nd number is " +str(b))

#select operator
operation=input("what type of operation do you want? \n")
print("you selected operation " +operation)

result = float(0)
#execute operation
if "add" in operation:
 	result= float(a+b)
if "subtract" in operation:
	result= float(a-b)
if "multiply" in operation:
 	result= float(a*b)
if "divide" in operation:
	result= float(a/b)
if "log" in operation:
	result= float(math.log(a,b))
if "sin" in operation:
    result= float(math.sin(a))
if "cos" in operation:
    result= float(math.cos(a))
if "power" in operation:
    result= float(a**b,b**a)
if "root" in operation:
    result= float(a**(1/b),b**(1/a))
print(result)
