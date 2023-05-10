"""V3 Turn into Function."""

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