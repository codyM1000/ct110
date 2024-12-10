# cody matheney
#10/31/2024
#p4lab2


# make a wwhile loop to control program running continuously
run_again= "yes"

while run_again=="yes" or run_again=="y":
    user_int=int(input("enter an interger: "))
    print()
    if user_int>=0:
        #print multplcation
        for num in range(1,13):
            print(f"{user_int}*{num}={user_int * num}")
        print()
    else:
        print("cannot accept negation values!!")
    
    run_again=input("would you like to run the program again? ").lower()
    valid_inputs=["yes","y","no","n"]
#validate the users input
    while run_again not in valid_inputs:
        print("INVALID RESONSE ENRERED!")
        run_again=input("would you like to run the program again? ").lower()
# loop breaks
print("exiting program...")










