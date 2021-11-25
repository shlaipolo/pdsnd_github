import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

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
    while True:
        city = input('\nWould you like to see data for Chicago, New York City or Washington?\n').lower()
        if city in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to explore? Please select either January, February, March, April, May, June or all.\n').lower()
        if month in months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day would you like to explore? Please select either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.\n').title()
        if day in days:
            break

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
    #load selected city csv file into a data frame
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time to datetime format to create new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #if filter by day selected
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month: ' + str(common_month))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day: ' + common_day)

    # TO DO: display the most common start hour
    common_hour = df['start_hour'].mode()[0]
    print('Most common start hour: ' + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start = df['Start Station'].mode()[0]
    print('Most commonly used start station: ' + most_used_start)

    # TO DO: display most commonly used end station
    most_used_end = df['End Station'].mode()[0]
    print('Most popular end station: ' + most_used_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_used_combo_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip: ' + str(most_used_combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ' + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ' + str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    except:
        print("\nThere is no gender info in the data of this city.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['Birth Year'].mode()[0])
        print('Earliest birth year: ' + str(earliest_birth))
        print('Most recent birth year: ' + str(most_recent_birth))
        print('Most common birth year: ' + str(most_common_birth))
    except:
        print("There is no user birth year info in the data of this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # ask if the user if they want to see 5 lines of raw data: display if 'yes', and next 5 lines and so on until answer is 'no'
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
    start_loc = 0

    while view_data != 'no':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to see the next five rows? Enter yes or no.\n").lower()


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

        #added this line for version control project

if __name__ == "__main__":
	main()
