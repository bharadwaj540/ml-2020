"""
1.Start with a greeting and asks user name
2.Greet user with his/her name
3.Bot displays what it can do[menu] and asks user to choose the operation
4.Responds to user inputs correctly
"""
# imported packages
import random
from datetime import datetime
from omdb import imdb_bot
from handCricket import hand_cricket
from rockPaperScissor import rock_paper_scissor
from evalexp import eval_exp
from curtime import cur_time
from greetings import greeting_bot


# wishes with respect to time with user name
def welcome(name):
    print(f"{cur_time()} {name}")

# list of things bot can do


def menu():
    print("Things that I can do")
    print("1.Calculate an expression")
    print("2.Get current time")
    print("3.Play Rock-Paper-Scissor")
    print("4.Play Hand Cricket")
    print("5.IMDB bot")
    print("6.End chat")
    print("-------------------")
    # If user enter any choice other than 1,2,3,4,5 and 6,it asks user to enter choice from [1-6]
    try:
        return int(input("Enter your choice[1-6] :"))
    except:
        print("Enter choice from 1,2,3,4,5 and 6")


def bot():
    greeting_bot()
    name = input("Enter your name: ")  # takes user name as a string
    welcome(name)
    choice = menu()
    while(choice != 6):
        if(choice == 1):
            eval_exp()  # calling eval_exp() from evalexp.py
        elif choice == 2:
            # datetime.now() is from datetime package
            print("Current time is:", str(datetime.now()))
        elif choice == 3:
            # calling eval_exp() from rockpaperscissor.py
            rock_paper_scissor(name)
        elif choice == 4:
            hand_cricket(name)  # calling hand_cricket() from handcricket.py
        elif choice == 5:
            imdb_bot()  # calling imdb_bot() from omdb.py
        else:
            # program terminates
            print("Please enter a number from 1,2,3,4,5 and 6")
        choice = menu()


bot()  # calling bot function
