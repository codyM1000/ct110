# matheney
#11/14/2024
#p5lab

import random

def calcCashBack():
    # genrate a random float for amountowned to store
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"you owe ${total_owed:.2f}")
    cash=float(input("how much cash will you put in the self-checkout? "))
    # calculat cash back
    cash_back=cash - total_owed
    return cash_back

    

def disperseCashBack(money):



    # considering if user put 0.00
    if money==0:
        print("no change")

    #check for debt
    if money <0:
        print("your in debt")
        
    if money >0:
        # convert money to a whole number
        money= int(round(money * 100,2))

        #print(money)

        # calculate the amount of dollars inthe money variable
        num_dollars = money//100
        #print(f"dollars:{num_dollars}")

        #remove the dollar from money variable
        money = money - (num_dollars*100)

        # caculate the amount of quarters in the money variable
        num_quarters = money//25

        #print (f"quarters:{num_quarters}")


        #remove the quarters from money variable
        money = money - (num_quarters*25)

        #remove dimes
        num_dimes=money//10

        #print(f"dimes:{num_dimes}")

        money=money-(num_dimes*10)

        #remove nickel
        num_nickel=money//5
        #print(f"nickel:{num_nickel}")
        money = money-(num_nickel*5)

        #remove pennies
        num_pennies=money
        #print(f"pennies:{num_pennies}")

    else:
        num_dollars=0
        num_quarters=0
        num_dimes=0
        num_nickel=0
        num_pennies=0

    # dollars
    if num_dollars>0:
        if num_dollars==1:
            print(f"{num_dollars} dollar")
        else:#variable is greater
            print(f"{num_dollars} dollars")

    # quarters
    if num_quarters>0:
        if num_quarters==1:
            print(f"{num_quarters} quartersr")
        else:#variable is greater
            print(f"{num_quarters} quarters")

    # dimes
    if num_dimes>0:
        if num_dimes==1:
            print(f"{num_dimes} dimes")
        else:#variable is greater
            print(f"{num_dimes} dimes")

    # nickel
    if num_nickel>0:
        if num_nickel==1:
            print(f"{num_nickel} nickel")
        else:#variable is greater
            print(f"{num_nickel} nickel")

    # pennies
    if num_pennies>0:
        if num_pennies==1:
            print(f"{num_pennies} pennies")
        else:#variable is greater
            print(f"{num_pennies} pennies")



#define main
def main():
    print(" welcome to the self check-out!!!***** ")
    cash_back = calcCashBack()
    print(f"change is ${cash_back:.2f}")
    disperseCashBack(cash_back)
    
    
# call the main
if __name__ =="__main__":
    main()
















