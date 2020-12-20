import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """ Gets input from user an creates variables to filter the dataset by.

    Parameters:
        None

    Returns:
        city (str) -- name of the city
        month (str) -- name of the month
        day (str) -- name of the day
    """
    print("\nWelcome to this project. In the following you can analyse descriptive statistics"
    " about bikeshare data from the company 'Motivate'.")

#get the city filter from the user
    city = ""
    while city not in CITY_DATA.keys():
        print("\nAs a first step you can select the city whose data you want to analyze")
        print("\nYou can choose between 1) Chicago, 2) New York City and 3) Washington")
        city = input("\nPlease enter your decision: ").lower()

        if city not in CITY_DATA.keys():
            print("\nThis is not a valid city name for this analysis.\n\n")
            print("\nTry again...\n")

    print(f"\nPerfect, you have choosen {city} as your city to conduct"
    " the analysis on.\n\n")


#get the month filter by the user
    months = ["all", "january", "february", "march", "april", "may", "june"]
    month=""

    while month not in months:
        print("\nNow you can coose the month to conduct the analysis on.")
        print("\nIf you want to analyse all the months, please enter: all.")
        print("\nIf you want to analyse a specific month enter the relevant name. "
        "You can choose between january, february, march, april, may"
        " or june.")
        month = input("\n Please enter your decision: ".lower())

        if month not in months:
            print("\nThis is not a valid month you can choose from.\n\n")
            print("\nTry again...\n")

    print(f"\n Perfect, you have choosen {month} as your month.\n\n")



#get the day filter by the user
    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday",
    "saturday", "sunday"]
    day = ""

    while day not in days:
        print("\nNow you can coose the day to conduct the analysis on.")
        print("\nIf you want to analyse all the days, please enter: all.")
        print("\n If you want to analyse a specific day enter the relevant name"
        " You can choose between monday, tuesday, wednesday, thursday, friday, saturday and sunday.")

        day = input("\n Please enter your decision: ".lower())

        if day not in days:
            print("This is not a valid month yo can choose from.\n\n")
            print("\nTry again...\n")

    print(f"\n Perfect, you have choosen {day} as your day.")


    print('-'*40)
    return city, month, day
