"""EndResults is asking if they want to see there summary on there score and averages"""

#Summary of quiz

#this is for testing
Points=int(input("how many points less then 10"))

#If you get no points
if Points=="0":
    print("you did your best but not good enough")

#If you get between 1-3 Points
if Points >=1 and Points <=3:
    print("you are not good at this")

#if you get between 4-6 points
if Points >=4 and Points <=6:
    print("not bad")

#if you get 7-9 pointd
if Points >= 7 and Points <= 9:
    print("your pretty good")

#if you get 10 points
if Points==10:
    print("Greatest of all time")