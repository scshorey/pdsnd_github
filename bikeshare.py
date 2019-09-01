import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS_INDEX = {"january": 1,
               "february": 2,
               "march": 3,
               "april": 4,
               "may": 5,
               "june": 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "new york city", "washington"]
    while True:
        city=input("What city would you like to analyze?: ").lower()
        if city in cities:
            print(f"You selected {city}")
            break
        else:
            print("Please choose Chicago, New York or Washington")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]   
    while True:
        month=input("Please specify a month: ").lower()
        if month in months:
            print(f"You selected {month}")
            break
        else:
            print("Please select a month from January to June or select all")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]   
    while True:
        day=input("Please specify a day of the week: ").lower()
        if day in days:
            print(f"You selected {day}")
            break
        else:
            print("Please choose a day of the week or select all")
            continue

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    lst = [city, month, day]
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if not month == "all":
        df = df[df['month'] == MONTHS_INDEX[month]]
       
    if not day == "all":
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    monthnames = list(MONTHS_INDEX.keys())
    popular_month = monthnames[df['month'].mode()[0] - 1].title()
    print(f"Most popular month: {popular_month}")

    # TO DO: display the most common day of week
    print(f"Most popular day: {df['day_of_week'].mode()[0]}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(f"Most popular hour: {df['hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"Most popular start station: {df['Start Station'].mode()[0]}")


    # TO DO: display most commonly used end station
    print(f"Most popular end station: {df['End Station'].mode()[0]}")
   

    # TO DO: display most frequent combination of start station and end station trip
    df2 = pd.DataFrame({"combo_station": df['Start Station'].map(str) + " to " + df['End Station']})  
    print(f"Most popular station combination: {df2['combo_station'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = time.strftime("%H Hours, %M Minutes and %S Seconds", time.gmtime(
        df['Trip Duration'].sum()))
    print(f"Total Travel Time: {total_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time = time.strftime("%H Hours, %M Minutes and %S Seconds", time.gmtime(
        df['Trip Duration'].mean()))
    print(f"Mean Travel Time: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"User type counts: \n{df['User Type'].value_counts().to_string()}\n")

    # TO DO: Display counts of gender
    try:
        print(f"Gender user counts: \n{df['Gender'].value_counts().to_string()}\n")
    except KeyError:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print(f"Eldest User Birth Year: {int(df['Birth Year'].min())}")
        print(f"Youngest User Birth Year: {int(df['Birth Year'].max())}")
        print(f"Most Common User Birth Year: {int(df['Birth Year'].mode()[0])}")
    except KeyError:
        print("Washington data doesn't have Birth Year")
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)        
        trip_duration_stats(df)
        user_stats(df)        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
