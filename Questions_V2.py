"""Fix the error where rounds would go up only if you get the question right
also made it look more clean"""

Points=0
Rounds=0

#Questions go here

#question_1
Rounds += 1
print(f"round {Rounds}")
quest_1=input("what is Tahi in english? ").lower()
if quest_1== "1" or quest_1== "one":
    print(f"you got it right it is {quest_1} ")
    Points+=1
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
if quest_6 == "Tekau":
    print(f"you got it right it is {quest_6} ")
    Points += 1
    Rounds += 1
    print(f"you have {Points} Points")
else:
    print("you suck thats wrong")
    print(f"you have {Points} Points")


# question_7
Rounds += 1
print()
print(f"round {Rounds}")
quest_7 = input("what is the first 3 numbers in maori(in order with a space in between them)? ").lower()
if quest_7 == "tahi rua toru":
    print(f"you got it right it is {quest_} ")
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
else:
    print("you suck thats wrong")
    print(f"you have {Points} Points")