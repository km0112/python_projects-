"""Write a program to prompt the user for hours and rate per hour
using input to compute gross pay. Pay should be the normal rate
for hours up to 40 and time-and-a-half for the hourly rate for
all hours worked above 40 hours. Put the logic to do the
computation of pay in a function called
computepay() and use the function to do the computation."""


def compute_pay():
    answer = input("Do you want to know your total earnings [Y/n]?: ")
    while answer.lower().startswith("y"):
        name = input("What is your name: ")
        print("Welcome", name)
        hrs = int(input("How many hours did you work? "))
        payrate = float(input("How much do you earn per hour? "))
        if hrs <= 40:
            profit = hrs * payrate
            print("You earned", profit, "dollars")
        elif hrs > 40:
            profit = 40 * payrate
            overtime = (hrs - 40) * (1.5 * payrate)
            print("You earned", overtime + profit, "dollars")
        # answer=input('Do you want to know your total earnings? type yes to use program')
        terminateloop = input("Do you want to end the loop?")
        if "yes" in terminateloop:
            break


# computepay()
def make_shirt():
    S = input("what size is the shirt?")
    text = input("what do you want printed on the shirt?")
    print("Your shirt is size", S, ",it says", text)


# make_shirt()
if __name__ == "__main__":
    compute_pay()
