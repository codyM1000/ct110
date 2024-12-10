# cody matheney
#p3lab
#10/17/2024

'''
#regular divsion
print(100/3)

# floor divsion
print(100/3)

# modulus divsion
print(100%3)
print(7%4)
'''

#get money from user as a float
money=float(input("enter the amount of money as a float: $"))

# considering if user put 0.00
if money==0:
    print("no change")

#check for debt
if money <0:
    print("your in debt")
    
if money >0:
    # convert money to a whole number
    money= round(money * 100)

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
