def Points():
    Points = 0
    Rounds = 0

    # Questions go here

    # question_1
    Rounds += 1
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
    print(f"round {Rounds}")
    quest_1 = input("what is Tahi in english? ").lower()
    if quest_1 == "1" or quest_1 == "one":
        print(f"you got it right it is {quest_1} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_3
    print(f"round {Rounds}")
    quest_1 = input("what is Tahi in english? ").lower()
    if quest_1 == "1" or quest_1 == "one":
        print(f"you got it right it is {quest_1} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_4
    print(f"round {Rounds}")
    quest_1 = input("what is Tahi in english? ").lower()
    if quest_1 == "1" or quest_1 == "one":
        print(f"you got it right it is {quest_1} ")
        Points += 1
        print(f"you have {Points} Points")
    else:
        print("you suck thats wrong")
        print(f"you have {Points} Points")

    # question_5
    # ...

    # question_6
    # ...

    # question_7
    # ...

    # question_8
    # ...

    # question_9
    # ...

    # question_10
    # ...

    return Points

final_points = Points()
print(f"Final Points: {final_points}")
