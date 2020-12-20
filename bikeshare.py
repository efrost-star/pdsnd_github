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

def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Parameters:
        df -- dataframe

    Returns:
        None
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

   # TO DO: display the most common month
    #calculate the mode value of the column month
    common_month = df["month"].mode()[0]
    #get the common month name as a string
    if common_month == 1:
        common_month_name = "January"
    elif common_month == 2:
        common_month_name = "February"
    elif common_month == 3:
        common_month_name = "March"
    elif common_month == 4:
        common_month_name = "April"
    elif common_month == 5:
        common_month_name = "May"
    elif common_month == 6:
        common_month_name = "June"


    print(f"Most common month: {common_month_name}")

    # TO DO: display the most common day of week
    #calculate the mode value of the column
    common_day = df["day_of_week"].mode()[0]

    print(f"Most common day: {common_day}")

    # TO DO: display the most common start hour
    #create new column with the hours
    df["hour"]=df["Start Time"].dt.hour
    #calculate the mode value of the column
    common_hour = df["hour"].mode()[0]

    print(f"Most common hour: {common_hour}")

    #Print time it took to calculate
    print("\nThis took%s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Parameters:
        df -- dataframe

    Returns:
        None
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #get the name of the most common station
    common_start_station = df['Start Station'].mode()[0]

    #get the count of the unique stations and the maximum value
    start_station_count = df["Start Station"].value_counts()
    common_start_station_count = start_station_count.max()

    print(f"The most common start station is {common_start_station} with the count of {common_start_station_count}.")


    # TO DO: display most commonly used end station
    #get the name of the most common station
    common_end_station = df['End Station'].mode()[0]

    #get the count of the unique stations and the maximum value
    end_station_count = df["End Station"].value_counts()
    common_end_station_count = end_station_count.max()

    print(f"The most common end station is {common_end_station} with the count of {common_end_station_count}.")

    # TO DO: display most frequent combination of start station and end station trip
    # create new column with combination of Start and End Station and calculate the mode of that column
    df["Start End Combination"] = df["Start Station"] +" - "+ df["End Station"]
    common_StartEnd_combination = df["Start End Combination"].mode()[0]

    print(f"The most common combination of Start and End Station is: {common_StartEnd_combination}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Parameters:
        df -- dataframe

    Returns:
        None
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #calculate the sum of travel time seconds
    total_duration = int(df["Trip Duration"].sum())
    duration = datetime.timedelta(seconds = total_duration)

    print(f"The total travel time was {duration} hours.")

    # TO DO: display mean travel time
    #calculate the mean of travel time
    mean_duration = int(df["Trip Duration"].mean())
    mean_duration = datetime.timedelta(seconds = mean_duration)

    print(f"The mean travel time was {mean_duration} minutes.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users.

    Parameters:
        df -- dataframe
        city (str) -- the city the data is filtered by

    Returns:
        None
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #count unique values of user types
    user_type = df["User Type"].value_counts()

    print("Your dataset has the following user type frequencies:\n")
    print(user_type)

    # TO DO: Display counts of gender
    #code returns except statement if dataset does not have the relevant column

    if city != "washington":
        gender = df["Gender"].value_counts()

        print("\nYour dataset has the following gender distribution:\n")
        print(gender)


    # TO DO: Display earliest, most recent, and most common year of birth
     #code returns except statement if dataset does not have the relevant column

        min_year = int(df["Birth Year"].min())
        max_year = int(df["Birth Year"].max())
        common_year = int(df["Birth Year"].mode())

        print(f"\nThe earliest Birth Year is {min_year}, the most recent Birth Year is {max_year} and the most common year of birth is {common_year}.")


    elif city == "washington":
        print("\nThis dataset has no data on Gender or Birth Year. ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def load_raw_data(city):
    """Loads the raw data set inly filtered by the selected city.

    Parameters:
        city (str) -- name of the city

    Returns:
        df_raw -- raw dataset filtered by city
    """
    df_raw = pd.read_csv(CITY_DATA[city])

    return df_raw

def raw_data(df_raw):
    """Displays rows from the raw data set

    Parameters:
        df_raw -- raw dataset filtered only by city

    Returns:
        None
    """

    #create empty variable to store the answer from the user
    #create list of valid responses
    #create empty row variable to store count of the rows
    answer = ""
    responses = ["yes", "no"]
    row = 0

    #show head of the raw data set if user chooses "yes"
    while answer not in responses:
        answer = input("Do you want to view the raw data set before you proceed? Enter yes or no:").lower()

        if answer == "yes":
            print(df_raw.head())

        elif answer not in responses:
            print("\nThis is not a valid response.")
            print("\nTry again...")

    #continue to show 5 more rows until user chooses "no"
    while answer == "yes":

        print("\nDo you want to see further lines from the raw data?")
        answer = input(("\nEnter yes or no: ")).lower()

        #while loop to handle wrong input
        while answer not in responses:
            print("\nThis is not a valid response.")
            print("\nTry again...")
            answer = input(("\nEnter yes or no: ")).lower()

        if answer == "yes":
            row += 5
            print(df_raw.loc[row:row+5])
        elif answer == "no":
            break

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df_raw = load_raw_data(city)

        raw_data(df_raw)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
