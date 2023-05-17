
# Greetings function
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

# rules function
def rules_Explained():
    print(
        "Welcome to my Māori number quiz. Here you will learn the maori numbers from 1-10" "it will be not to difficult")
    print()
    # explain how the rules work and how to get points
    print("To play the Māori Quiz you need to read what the question they asked was and write the correct answer")
    print("if it is the correct answer you will gain 1 point and move up however if you dont choose the write ")
    print("answer you will not gain a point ")
    return ""


#Questions Function
def Questions():
    Points = 0
    Rounds = 0

    # Questions go here

    # question_1
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_1 = input("what is Tahi in english? ").lower()
    if quest_1 == "1" or quest_1 == "one":
        print(f"you got it right it is {quest_1} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_2
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_2 = input("what is Rua in english? ").lower()
    if quest_2 == "2" or quest_2 == "two":
        print(f"you got it right it is {quest_2} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_3
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_3 = input("what is Rima in english? ").lower()
    if quest_3 == "five" or quest_3 == "5":
        print(f"you got it right it is {quest_3} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_4
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_4 = input("what is ono in english? ").lower()
    if quest_4 == "6" or quest_4 == "six":
        print(f"you got it right it is {quest_4} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_5
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_ = input("what does Rima + Wha equal in english? ").lower()
    if quest_ == "9" or quest_ == "nine":
        print(f"you got it right it is {quest_} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_6
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_6 = input("what is 10 in Maori? ").lower()
    if quest_6 == "tekau":
        print(f"you got it right it is {quest_6} ")
        Points += 1
        Rounds += 1
        print(f"you have {Points} Points")
    else:
        print("you suck that's wrong")
        print(f"you have {Points} Points")

    # question_7
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_7 = input("what is the first 3 numbers in maori(in order with a space in between them)? ").lower()
    if quest_7 == "tahi rua toru":
        print(f"you got it right it is {quest_7} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_8
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_8 = input("what does 5-3 equal in Maori? ").lower()
    if quest_8 == "rua":
        print(f"you got it right it is {quest_8} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_9
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_9 = input("what is iwa in english? ").lower()
    if quest_9 == "9" or quest_9 == "nine":
        print(f"you got it right it is {quest_9} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_10
    Rounds += 1
    print()
    print(f"round {Rounds}")
    quest_10 = input("what does 10-2+3-8 equal in Maori? ").lower()
    if quest_10 == "toru":
        print(f"you got it right it is {quest_10} ")
        Points += 1
        print(f"you have {Points} Points")
        return Points
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")
        return Points

#Summary
def Summary():
    # Summary of quiz
    # If you get no points
    if PointsGained == "0":
        print(f"You got {PointsGained}")
        print("you did your best but not good enough")

    # If you get between 1-3 Points
    if PointsGained >= 1 and PointsGained <= 3:
        print(f"You got {PointsGained}")
        print("you are not good at this")

    # if you get between 4-6 points
    if PointsGained >= 4 and PointsGained <= 6:
        print(f"You got {PointsGained}")
        print("not bad")

    # if you get 7-9 pointd
    if PointsGained >= 7 and PointsGained <= 9:
        print(f"You got {PointsGained}")
        print("your pretty good")

    # if you get 10 points
    if PointsGained == 10:
        print(f"You got {PointsGained}")
        print("Greatest of all time")

#Accuracy
def Accuracy():
    # Accuracy
    Accuracy = PointsGained
    Accuracy *= 10
    perfectscore = 10 - PointsGained
    if perfectscore == 0:
        print("You were amazing")
    else:
        print(f"You were close you needed {perfectscore} more points to get a perfect score")
        print(f"You got {Accuracy}%")


def formatter(symbol,text):
    sides = symbol * 1
    formatted_text = f"{sides}{text}{sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{text}\n{top_bottom}"

# Main routine
print(formatter("%", "welcome to the maori quiz"))
played_before = yes_no("have you played")
PointsGained = Questions()
print()
print(formatter("#","Here is the summary of the quiz"))
Summary()
Accuracy()
