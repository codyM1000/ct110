#we are about to create user-defined functions


# defined a non value returning function
def my_animal(name, sound, pound_food):
    print(f"the {name} makes a {sound} noise!")
    print(f"the{name} eats {pound_food} pounds of food a day")
    print(f"the{name} eats {(pound_food * 7):.2f} pounds of food a week")

def getName():
    name=input("enter your name: ")
    return name + "*******"

def displayName(first):
    lastName=input("enter your last name: ")
    fullName=first+""+lastName
    return fullName

# create a main function - all logic goes here
def main():
    print("main function is executing!")
    print()
    # call
    my_animal("lion","rawwwer",20.5)
    print()
    my_animal("mouse","ekekekekek",0.2)

    #call the  value return function
    myName=getName()
    print(myName)
    print()
    print(displayName(myName))

# call the main function
if __name__=="__main__":
    main()


