A=input('Do you want to run this program?')

while A == 'yes':
    ans=input('Do you want to convert weight or temperature?')
    if 'weight' in ans:
        N=input('Do you want to convert kg or lb?')

        if 'kg' in N:
            kg1= int(input('How many kilograms?'))
            lb1= kg1*2.2
            print (lb1)
            print('Your amount of kilograms is',lb1,'pounds')

        elif 'lb' or 'pounds' in N:
            lb2= int(input('How many pounds?'))
            kg2= lb2/2.2
            print (kg2)

    elif 'temp' in ans:
        ans1=input('Do you want to convert Celsius, Farenheit, or Kelvins?')
        if 'C' in ans1:
            C=float(input('Please enter degrees in Celsius'))
            F=(1.8*C)+32
            K=C+273.5
            print(C,F,K)
        elif 'F' in ans1:
            F=float(input('Please enter degrees in Farenheit'))
            C=(F-32)*(5/9)
            K=(F-32)*(5/9)+273.15
            print(F,C,K)
        elif 'K' in ans1:
            K=float(input('Please enter degrees in Kelvin'))
            C=K-273.5
            F=(K-273.15)*(9/5)+32
            print(K,C,F)

    A=input('Do you want to run this program again?')
