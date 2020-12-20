# Date created
This project was created on the **14.12.2020**.

# Explore US Bikeshare Data
This is a project from the "Programming fo Data Science" course from Udacity.

## Overview
In this project, I used Python to explore data related to bike share systems for three major cities in the United States:\
- Chicago
- New York City
- Washington

I wrote code to import the data and answered questiions about it by computing descriptive statistics.\
The script takes raw input.

## Software

For this project I used:
- python 3.9
- text editor
- terminal application

### Python Packages

In this project the following packages were used:

- time
- datetime
- numpy
- pandas  

## Datasets

The data was provided by the company [Motivate](https://www.motivateco.com/). A bike share system provider for many major cities in the United States.\
The datasets contain randomly selected data for all **three cities** for the first six months of 2017.  All three of the data files contain the same core six (6) columns:
- **Start Time** (e.g., 2017-01-01 00:07:57)
- **End Time** (e.g., 2017-01-01 00:20:53)
- **Trip Duration** (in seconds - e.g., 776)
- **Start Station** (e.g., Broadway & Barry Ave)
- **End Station** (e.g., Sedgwick St & North Ave)
- **User Type** (Subscriber or Customer)

The _Chicago_ and _New York City_ files also have the following two columns:

- **Gender**
- **Birth Year**

## Statistics Computed

The code provides the following information:

**1 Popular times of travel (i.e., occurs most often in the start time)**
- most common month
- most common day of week
- most common hour of day

**2 Popular stations and trip**
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

**3 Trip duration**
- total travel time
- average travel time

**4 User info**
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Handling raw input and filtering the dataset

By entering input, the user can decide which data set he or she would like to view in terms of descriptive statistics. The user can also filter the selected data set by a specific month and day. After selecting the filters, the user can also view the raw data of the selected data set, if desired.

## Get started

To get the code started just navigate in your terminal to the directory where the project is located
and type `python bikeshare.py`. (If you are using a newer version of python remeber to type _python 3_!).
After this the code will ask you for input to select the filters.
