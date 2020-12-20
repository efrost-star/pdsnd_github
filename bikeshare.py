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

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Parameters:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data into dataframe
    print("Loading your selected data set...\n")
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to creat new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

     # filter by month if applicable
    if month != "all":
        #user the index of the months list to get the corresponding int
        months=["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by month if applicable
    if day != "all":
        #filter by day to get the new dataframe
         df = df[df['day_of_week'] == day.title()]

    return df
