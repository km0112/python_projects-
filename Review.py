#Scheduling program
hrs1=0
answer=input('Do you want to know your calendar?')
while answer == 'yes':
    n=int(input('How many events do you have today?'))
    for n in range (1,n):
        event=input('What do you have to do?')
        hrs=float(input('How many hours long is the event?'))
        hrs1=hrs
#24-7=17 so this accounts for 7 hrs of sleep
    if hrs1==0:
        print('Enjoy your day off')
    elif hrs1<=17:
        print(float('You have',hrs,'hrs of work and',17-hrs,'hrs of downtime with 7 hrs of sleep'))
    elif hrs1>17:
        print('There is literally not enough time in the day')

    A=input('Do you want to add another calendar?')
    #answer=input('Do you want to know your total earnings? type yes to use program')
