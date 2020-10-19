# return current time
import random
from datetime import datetime


def cur_time():
    current_time = datetime.now().hour
    greeting = "Good Morning"
    if(current_time >= 22):
        greeting = "It`s too late"
    elif(current_time >= 17):
        greeting = "Good Evening"
    elif(current_time >= 12):
        greeting = "Good Afternoon"
    return greeting
