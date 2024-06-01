A=input('Do you want to run this program?')

while A == 'yes':

    ans1=input('Do you want to convert kilograms to pounds?')
    ans2=input('Do you want to convert pounds to kilograms?')
    if ans1 == 'no' and ans2 == 'no':
        break
    while ans2 == 'no' and ans1 == 'yes':
        kg1= int(input('How many kilograms?'))
        lb1= kg1*2.2
        print (lb1)
        print('Your amount of kilograms is',lb1,'pounds')
        break
        #if 'yes' in terminateloop:
            #break
    while ans2 == 'yes' and ans1 == 'no':
        lb2= int(input('How many pounds?'))
        kg2= lb2/2.2
        print (kg2)
        #terminateloop=input('Do you want to end the loop?')
        #if 'yes' in terminateloop:
            #break



"'for i in range (0,5) i=0 while i<max i=i+1'"
