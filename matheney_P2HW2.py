#cody matheney
#P2HW2
#10/10/2024


num1=float(input("enter grade for module 1: "))
num2=float(input("enter grade for module 2: "))
num3=float(input("enter grade for module 3: "))
num4=float(input("enter grade for module 4: "))
num5=float(input("enter grade for module 5: "))
num6=float(input("enter grade for module 6: "))


num_list=[]

num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
num_list.append(num5)
num_list.append(num6)

# grades and stuff

print(f"the lowest grade {min (num_list)} ")
print(f"the highest grade {max (num_list)} ")
print(f"the sum of the value is {sum(num_list)} ")
print(f"average grade {sum(num_list)/len(num_list):.2f}")



