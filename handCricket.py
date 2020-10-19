"""
RULES OF HANDCRICKET:
1.select batting or bowling
if batting:
    a.choose score from [0-6]
    b.add score to final user score
    b.if both bot and user chooses same score,thats out move to "c".Else repeate a,b
    c.now user bowls i.e,choose score from[1-6]
    d.add score to final bot score
    e.if both bot and user chooses same score,thats out move to "f",if final bot score is greater than user final score bot wins
        .Else repeate c,d
    f.check user final score and bot final score
    g.if user final score is greater than bot final score then user wins else bot wins

if bowling:
    a.choose score from [0-6]
    b.add score to final bot score
    b.if both bot and user chooses same score,thats out move to "c".Else repeate a,b
    c.now user bats i.e,choose score from[1-6]
    d.add score to final user score
    e.if both bot and user chooses same score,thats out move to "f",if final user score is greater than bot final score user wins
        .Else repeate c,d
    f.check user final score and bot final score
    g.if user final score is greater than bot final score then user wins else bot wins

"""


# handcricket game
import random
from datetime import datetime


class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
    # __str__ is to print() the value

    def __str__(self):
        return(repr(self.value))


def hand_cricket(name):
    scores = [0, 1, 2, 3, 4, 5, 6]
    print("Lets start the game...!!!")
    count1, count2 = 0, 0
    print("Select batting or bowling??")
    print("1.Batting")
    print("2.Bowling")
    choice = int(input("Select batting or bowling: "))
    # If player selects batting first
    if(choice == 1):
        player_score = int(
            input("Its your turn,you need to bat first,enter a number[0-6]:"))
        computer_score = random.choice(scores)

        while(computer_score != player_score):  # player batting
            if(player_score not in scores):
                #player_not in [0-6]
                try:
                    raise MyError(player_score)
                except MyError as error:
                    print(error.value, "is not allowed")
                    player_score = int(input(
                        "Please enter a number from 0,1,2,3,4,5 and 6:"))
                    continue
            # Gives output of ever single round details
            count1 += player_score
            print("You scored", player_score)
            print("Computer bowled", computer_score)
            print("Your total score is", count1)
            player_score = int(input("Its your turn,enter a number[1-6]"))
            computer_score = random.choice(scores)

        # if its out i.e,both chooses same score
        print("You and bot both scored", player_score,
              "That`s out!!! your batting ends here")
        print("Your total score is ", count1,
              ".Restrict bot score less than", count1, "to win the game")
        player_bowl = int(input("You need to bowl,Enter a number[0-6]:"))
        computer_bat = random.choice(scores)

        while(computer_bat != player_bowl):  # bot batting
            if(player_bowl not in scores):
                try:
                    raise MyError(player_bowl)
                except MyError as error:
                    print(error.value, "is not allowed")
                    player_bowl = int(input(
                        "Please enter a number from 0,1,2,3,4,5 and 6:"))
                    continue
            count2 += computer_bat
            print("Bot scored:", computer_bat)
            print("You bowled:", player_bowl)
            print("Bot total score:", count2)
            if(count2 > count1):
                print("Bot won the game.Better luck next time")
                break
            player_bowl = int(input("You need to bowl,Enter a number[0-6]:"))
            computer_bat = random.choice(scores)
        print("You and Bot both scored", player_bowl, "So the game ends here")
        print("Game over.Lets have a look at the results")
        print("Your total score:", count1)
        print("Bot total score:", count2)
        if(count1 >= count2):
            print("Congratulations!!You won the game")
            print("---------------------")
        else:
            print("Bot won the game.Better luck next time", name)
            print("---------------------")

    # If player selects bowling first
    elif choice == 2:
        player_bowl = int(input("You need to bowl,Enter a number[0-6]:"))
        computer_bat = random.choice(scores)
        while(computer_bat != player_bowl):  # Bot batting
            if(player_bowl not in scores):
                try:
                    raise MyError(player_bowl)
                except MyError as error:
                    print(error.value, "is not allowed")
                    player_bowl = int(input(
                        "Please enter a number from 0,1,2,3,4,5 and 6:"))
                    continue
            count2 += computer_bat
            print("Bot scored:", computer_bat)
            print("You bowled:", player_bowl)
            print("Bot total score:", count2)
            player_bowl = int(input("You need to bowl,Enter a number[0-6]:"))
            computer_bat = random.choice(scores)
        print("You and bot both scored", player_bowl,
              "That`s out!!")
        print("Bot total score is ", count2,
              ".You need to chase", count2, "to win the game")
        player_score = int(
            input("Its your turn,you need to bat ,enter a number[0-6]:"))
        computer_score = random.choice(scores)
        while(computer_score != player_score):  # player batting
            if(player_score not in scores):
                try:
                    raise MyError(player_score)
                except MyError as error:
                    print(error.value, "is not allowed")
                    player_score = int(input(
                        "Please enter a number from 0,1,2,3,4,5 and 6:"))
                    continue
            count1 += player_score
            print("You scored", player_score)
            print("Computer bowled", computer_score)
            print("Your total score is", count1)
            if(count2 < count1):
                print("Congratulations!!You won the game.")
                break
            player_score = int(input("Its your turn,enter a number[1-6]"))
            computer_score = random.choice(scores)
        print("You and Bot both scored", player_bowl, "So the game ends here")
        print("Game over.Lets have a look at the results")
        print("Your total score:", count1)
        print("Bot total score:", count2)
        if(count1 >= count2):
            print("Congratulations!!You won the game")
            print("---------------------")
        else:
            print("Bot won the game.Better luck next time", name)
            print("---------------------")
    else:
        print("---Please choose 1 or 2----")
        hand_cricket(name)
