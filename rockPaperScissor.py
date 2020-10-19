# Rock-Paper-Scissor Game
import random
"""
IMP POINTS:
1.Rules of rock-paper-scissor
    a.rock beats scissors
    b.paper beats rock
    c.scissor beats paper
2.User needs to choose the points to win,who ever first reaches the points wins the game
"""


def rock_paper_scissor(name):
    l = ["Rock", "Paper", "Scissor"]
    count, count1, count2 = 1, 0, 0
    # asking user to enter points to win
    points = int(input("Enter points to win: "))

    # bot asks user to choose among r,p,s till user or bot score reaches to points you choose
    while (count1 < points or count2 < points):
        player = input("Select your choice[R,P,S]: ")
        if(player in ["r", "p", "s", "R", "P", "S"]):  # if
            if player == "r" or player == "R":
                player = "Rock"
            if player == "p" or player == "P":
                player = "Paper"
            if player == "s" or player == "S":
                player = "Scissor"

            print("ROUND NO", count)
            count += 1
            print(f"{name}:", player)
            computer = random.choice(l)
            print("Bot:", computer)
            if(player == computer):  # if both user and bot chooses same,its a tie
                print("Ohh!it`s a tie")

            if(player == "Rock"):
                if(computer == "Scissor"):
                    count1 += 1
                elif(computer == "Paper"):
                    count2 += 1
                    print("I got a point.It seems I am winning the game...hahahha!!!")

            if(player == "Paper"):
                if(computer == "Rock"):
                    count1 += 1
                elif(computer == "Scissor"):
                    count2 += 1
                    print("I got a point.It seems I am winning the game...hahahha!!!")

            if(player == "Scissor"):
                if(computer == "Paper"):
                    count1 += 1
                elif(computer == "Rock"):
                    count2 += 1
                    print("I got a point.It seems I am winning the game...hahahha!!!")

            print("Your score:", count1)
            print("Bot score:", count2)

            # loop ends here if anyone reaches the target points
            if(count1 == points or count2 == points):
                break
        else:  # if user chooses other than r,p,s
            print("Enter choice from R,P and S")
    if(count1 > count2):
        print("Contratulations!!You won the game")
        print("---------------------")
    else:
        print("Bot won the game!!Better luck next time", name)
        print("---------------------")
