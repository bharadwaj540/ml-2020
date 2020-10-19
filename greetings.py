# greetings
import random
from datetime import datetime

# wishes user


def greeting_bot():
    responses = [
        "Hi!I am a math bot.May I please know your name?",
        "Hello there!Nice to see you.Could you please tell your name?",
        "May I know your name?"
    ]
    print(random.choice(responses))
