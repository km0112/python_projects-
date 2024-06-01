
answer=input('Do you want to know your total earnings? type yes to use program')
while answer == 'yes':
    name = input('What is your name')
    print('Welcome',name)
    hrs=int(input('How many hours did you work?'))
    payrate=int(input('How much do you earn per hour?'))
    if hrs<=40:
            profit= hrs*payrate
            print('You earned',profit,'dollars')
    elif hrs>40:
        profit=40*payrate
        overtime=(hrs-40)*(1.5*payrate)
        print('You earned',overtime+profit,'dollars')
    #answer=input('Do you want to know your total earnings? type yes to use program')
    terminateloop=input('Do you want to end the loop?')
    if 'yes' in terminateloop:
        break








    print(hrs)
