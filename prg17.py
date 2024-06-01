#airline entry program that inputs a username, uses a loop to assign them a seat number,
#asks them if they need a special meal or not, then prints out the name,
#their food designation and their seat number
import random

A=input('Do you want to get on this flight?')

while A == 'yes':

    ans1=input('What is your name?')
    ans2=input('Do you want a special meal?')

    if ans2=='no':
        ans3='nothing'
        print()
    elif ans2=='yes':
        ans3=input('What do you want to eat?')

    n=random.randint(1,172)

    print (ans1,"your seat number is",n,"and you ordered",ans3)

    #if ans2=='no':
        #print()
    #elif ans2=='yes':
        #print('You ordered',ans3)

    A=input('Do you want to enter another passenger?')
