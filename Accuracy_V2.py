"""Turn into Function"""

def Accuracy():
    # Accuracy
    Accuracy = PointsGained
    Accuracy /= 10
    print(Accuracy)
    perfectscore = 10 - PointsGained
    if perfectscore == 10:
        print("You were amazing")
    else:
        print(f"You were close you needed {perfectscore} more points to get a perfect score")