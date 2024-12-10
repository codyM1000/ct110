#cody matheney
#9/17/2024
#P1HW1
#Input output with mathematical expressions

print("-----calculating Exponents------")
print()
print()

# Get base value (as an integer) from the user
base_value=int(input("enter an integer as a base value: "))

# Get exponent value from user
exponent=int(input("enter an integer as the exponet: "))

# Raise the base_value to the exponet
value = base_value**exponent

print()
print()

#display output to the user
print(base_value, "raise to the power of", exponent, "is", value, "!!")

print()
print()
print("------Addition and  Subtraction-------")
print()
print()

start_num = int(input("enter a starting integer: "))
add_num = int(input("enter an integer to add: "))
sub_num = int(input("enter an integer to subtract: "))

print()
print()

print(start_num,"+", add_num, "-", sub_num, "is equal to", start_num + add_num - sub_num)
