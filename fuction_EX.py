#we are about to create user-defined functions


# defined a non value returning function
def my_animal(name, sound, pound_food):
    print(f"the {name} makes a {sound} noise!")
    print(f"the{name} eats {pound_food} pounds of food a day")
    print(f"the{name} eats {pound_food * 7} pounds of food a week")


# create a main function - all logic goes here
def main():
    print("main function is executing!")
    print()
    # call
    my_animal("lion","rawwwer",20.5)
# call the main function
if __name__=="__name__":
    main()


