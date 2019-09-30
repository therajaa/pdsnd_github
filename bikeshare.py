#It is pretty simple as I divided subsections with functions
#Here is the code for the bikehire data analysis with python
#This was the second project for the Udacity's Nanodegree Course
import time
import pandas as pd




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

        
    while True:
      city_a = input("\nWhich city would you like to explore?: Please ENTER 'Chicago', 'New York City' or 'Washington'?\n")
      city=city_a.lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Kindly Enter a valid City: City can only be 'Chicago', 'New York City' or 'Washington'")
        continue
      else:
        break
        
    # get user input for month (all, january, february, ... , june)

    
    while True:
      month_a = input("\nWould you like to filter by month?: Please ENTER a month between 'January' to 'June' or ENTER 'ALL' if you do not have any preference.\n")
      month = month_a.lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Kindly ENTER a valid Month  or 'all' to continue.")
        continue
      else:
        break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    
    while True:
      day_a = input("\nWould you like to filter by day of the week?: Please ENTER a day between 'Monday' to 'Sunday' or ENTER 'ALL' if you do not have any preference.\n")
      day = day_a.lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Kindly Enter a valid Day  or 'all' to continue.")
        continue
      else:
        break

    print('-'*25)
    return city, month, day


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
    
       # load data into dataframe using pandas
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column in the dataframe into datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Pull out the month and day of week from Start Time

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    popular_month = df['month'].mode()[0]
    print('Most Common month:', popular_month)


    # display the most common day of week
    
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)


    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    most_start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used "Start-station":', most_start_station)



    # display most commonly used end station
    
    most_end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used "End-station":', most_end_station)


    # display most frequent combination of start station and end station trip
    
    most_start_end_combo = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of "Start-station" & "End-Station" trip:', 
    most_start_station, " & ", most_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time: {:.0f}  " days approx.".' .format(total_travel_time/(60*60*24)))


    # display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print('Type of users:\n', user_types)


    # Display counts of gender
    
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data.")
    
    

    # Display earliest, most recent, and most common year of birth
    
    try:
      earliest_year = df['Birth Year'].min()
      print('\nEarliest Year:', earliest_year)
    except KeyError:
      print("\nEarliest Year:\nNo data.")

    try:
      most_recent_year = df['Birth Year'].max()
      print('\nMost Recent Year:', most_recent_year)
    except KeyError:
      print("\nMost Recent Year:\nNo data.")

    try:
      most_common_year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', most_common_year)
    except KeyError:
      print("\nMost Common Year:\nNo data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df):
    #Inquire the USER to see a brief sample of the DATA
    
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWant to see some sample of the data-list?: Please '
                        'ENTER \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Invalid input, kindly ENTER 'YES' or"
                  " 'NO'.")
    if display.lower() == 'yes':
        print(df[df.columns[:]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more'
                                     ' trip data? ENTER \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Invalid input, kindly ENTER 'YES' or"
                  " 'NO'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[:]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break
   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nWould you like to perform another SEARCH? Enter 'yes' or 'no'.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

