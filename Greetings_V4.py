"""Greeting_V3 turing them into functions"""


#Greetings function
def yes_no(Rules):
    Rules_Explained = ""
    while Rules_Explained != "x":
        # ask user if they have played the game before
        Rules = input("have you played this game before?: ").lower()

        # If 'yes' program continues
        if Rules == "yes" or Rules == "y":
            return True

        # if they say no explain rules
        if Rules == "no" or Rules == "n":

            # greetings and explaining how it works
            print(rules_Explained())
            return False

        # other whill print "please answer 'yes' and 'no'
        else:
            print("please enter 'yes' or 'no'")




#rules function
def rules_Explained():
    print(
        "Welcome to my Māori number quiz. Here you will learn the maori numbers from 1-10" "it will be not to difficult")
    print()
    # explain how the rules work and how to get points
    print("To play the Māori Quiz you need to read what the question they asked was and write the correct answer")
    print("if it is the correct answer you will gain 1 point and move up however if you dont choose the write ")
    print("answer you will not gain a point ")

#Main routine
played_before=yes_no("have you played")