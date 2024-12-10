#
#cody matheney
#10/3/2024
#

#creat dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

#get the key only
keys = cars.keys()
print(keys)
print()

#prompt the user to give one of the keys (cars)
user_choice=input("enter a vehicle to see it's mpg: ")
print()

#show use mpg for their selected car
print(f"the {user_choice} gets{cars[user_choice]} mpg.")

#get amount of miles tobe driven
miles_to_drive=float(input(f"how mant miles will you drive the {user_choice}?"))

#callculate gallons needed to drive distance
gallons_needed=miles_to_drive/cars[user_choice]

#display gallons needed to user
print(f"{gallons_needed:.2f}gallons of gas needed to drive the {user_choice} {miles_to_drive} miles.")
