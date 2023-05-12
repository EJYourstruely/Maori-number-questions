# Greetings function
def yes_no():
    while True:
        # ask user if they have played the game before
        rules = input("Have you played this game before? (yes/no): ").lower()

        if rules == "yes" or rules == "y":
            return True
        elif rules == "no" or rules == "n":
            rules_explained()
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Rules function
def rules_explained():
    print("Welcome to my Māori number quiz. Here, you will learn the Māori numbers from 1 to 10.")
    print("To play the Māori Quiz, read the question and provide the correct answer.")
    print("Each correct answer earns you 1 point.")

# Questions Function
def questions():
    points = 0
    rounds = 0

    # Questions
    def ask_question(question, answer):
        nonlocal points
        nonlocal rounds
        rounds += 1
        print(f"\nRound {rounds}")
        user_answer = input(question).lower()

        if user_answer == answer:
            points += 1
            print(f"You got it right! The answer is '{answer}'.")
            print(f"You have {points} point(s).")
        else:
            print(f"That's incorrect. The answer is '{answer}'.")
            print(f"You have {points} point(s).")

    ask_question("What is 'tahi' in English? ", "one")
    ask_question("What is 'rua' in English? ", "two")
    ask_question("What is 'rima' in English? ", "five")
    ask_question("What is 'ono' in English? ", "six")
    ask_question("What does 'rima' + 'whā' equal in English? ", "nine")
    ask_question("What is 'tekau' in Māori? ", "ten")
    ask_question("What are the first three numbers in Māori (in order, separated by spaces)? ", "tahi rua toru")
    ask_question("What does 5 - 3 equal in Māori? ", "rua")
    ask_question("What is 'iwa' in English? ", "nine")
    ask_question("What does 10 - 2 + 3 - 8 equal in Māori? ", "toru")

    return points

# Summary
def summary(points_gained):
    print("\n--- Quiz Summary ---")
    print(f"You earned {points_gained} point(s).")

    if points_gained == 0:
        print("You did your best, but not good enough.")
    elif points_gained <= 3:
        print("You are not good at this.")
    elif points_gained <= 6:
        print("Not bad.")
    elif points_gained <= 9:
        print("You're pretty good!")
    else:
        print("Greatest of all time!")

# Accuracy
def accuracy(points_gained):
    accuracy = (points_gained / 10) * 100
    print(f"Accuracy: {accuracy}%")

# Main routine
played_before = yes_no()
if played_before:
    print("Great! Let's continue with the quiz.")
else:
    print("No problem! Here are the rules:")
    rules_explained()

points_gained = questions()
summary(points_gained)
accuracy(points_gained)
