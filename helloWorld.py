# helloworld.py

# Constants
GREETING = "Hello, "
FAREWELL = "Goodbye, "
MORNING_GREETING = "Good morning, "
AFTERNOON_GREETING = "Good afternoon, "
EVENING_GREETING = "Good evening, "

def greet(name):
    return GREETING + name

def farewell(name):
    return FAREWELL + name

def greet_with_time(name, time_of_day):
    if time_of_day == "morning":
        return MORNING_GREETING + name
    elif time_of_day == "afternoon":
        return AFTERNOON_GREETING + name
    elif time_of_day == "evening":
        return EVENING_GREETING + name
    else:
        return GREETING + name
