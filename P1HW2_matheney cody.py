# cody matheney
 # 9/26/2024
 # P1HW1
 # For this assignment you will create a program that does some basic math on numbers that are entered.

budget=float(input("enter budget:$"))
 
travel_destination=(input("enter travel destination"))

amount_spent_on_gas=float(input("enter the amount you will spend on gas:$"))

print(f"you will spend ${amount_spent_on_gas:.2f}on gas.")

amount_accommodation=float(input("enter amount for accommodation:$"))

amount_spent_on_food=float(input("enter amount spent on food:$"))

print("--------Travel Expenses--------")

print("location:", travel_destination)
print("budge:",budget)
      
print("fuel:",amount_spent_on_gas)
print("accomodation:",amount_accommodation)
print("food:",amount_spent_on_food)
      
#calculate amount of exspenses
      
money_leftover =(budget)-(amount_spent_on_gas)-(amount_accommodation)-(amount_spent_on_food)

print("remaining balance",money_leftover)

