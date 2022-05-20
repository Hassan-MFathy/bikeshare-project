import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filter():
    print("Hello! Let's explore some US bikeshare data!")
    cities = ('Chicago', 'New York', 'Washington')
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    days = ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    user_filter = ("month", "day", "both")
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? \n> ").title()

        selected_filter = input("would you like to filter the data by month, day or not at all? Type \"none\" for no time filter:  \n> ").lower()
        if(selected_filter == "month"):
                month = input("Please enter month: (e.g: 'january', 'february', 'march', 'april', 'may', 'june')  or type \"all\" to apply no month filter: \n> ").lower()
                day= False
        elif (selected_filter == "day"):
                day = input("Please enter day: (e.g: 1=Sunday) or type \"all\" to apply no day filter: \n> ")
                month = False
        elif (selected_filter == "both"):
                month = input("Please enter month: (e.g: 'january', 'february', 'march', 'april', 'may', 'june')  or type \"all\" to apply no month filter: \n> ").lower()
                day = input("Please enter day: (e.g: 1=Sunday) or type \"all\" to apply no day filter: \n> ")
                if(month == "all" and day == "all"):
                    month = True
                    day = "none"
                    print('-'*100)
                    print("You have chosen to filter data by both month and day, please enter the specified month and day")
        else:
            day = False
            month = False
        if (city in cities) and ((selected_filter in user_filter) or (selected_filter == "none"))  and (month == False or (month in months) or month == "all") and ( day == "all" or day == False or int(day) == days.index(days[int(day)])):
            break
    print('-'*100)

    return city, month, day, selected_filter

def load_data(city, month, day, selected_filter):
    months = ('january', 'february', 'march', 'april', 'may', 'june')
    selected_file = pd.read_csv(CITY_DATA[city])
    selected_file["Start Time"] = pd.to_datetime(selected_file["Start Time"])
    selected_file["month"] = selected_file["Start Time"].dt.month
    selected_file["day_of_week"] = selected_file["Start Time"].dt.dayofweek
    selected_file["hour"] = selected_file["Start Time"].dt.hour
    if(selected_filter == "month"):
        selected_file= selected_file.loc[selected_file["month"] == months.index(month) + 1]
    elif(selected_filter == "day"):
        selected_file = selected_file.loc[selected_file["day_of_week"] == int(day) - 1 ]
    
    elif (selected_filter == "both"):
        if month != "all":
            selected_file = selected_file.loc[selected_file["month"] == months.index(month) + 1]
        elif day != "all":
            selected_file = selected_file.loc[selected_file["day_of_week"] == int(day) - 1 ]


    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no \n')
    start_loc = 0
    keep_asking = True
    while (keep_asking):
        print(selected_file.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data == "no": 
            keep_asking = False

    
    return selected_file



def time_stats(selected_file, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

  
    # TO DO: display the most common month
    if month != "all" :
       months = ('january', 'february', 'march', 'april', 'may', 'june')
       common_month = selected_file["month"].mode()[0]
       print('Most common month:', months[common_month -1])

    # TO DO: display the most common day of week
    if day != "all":
       days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
       common_day = selected_file["day_of_week"].mode()[0]
       print('Most common day of week:', days[common_day])
    


    # TO DO: display the most common start hour
    common_hour = selected_file["hour"].mode()[0]
    print("the most common start hour", common_hour)
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def station_stats(selected_file):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start_station = selected_file['Start Station'].mode()[0]
    
    print("The most commonly used start station :", common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = selected_file['End Station'].mode()[0]
    print("The most commonly used end station :", common_end_station)



    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = selected_file[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(common_start_end_station[0], common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(selected_file):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = selected_file['Trip Duration'].sum()
    print("total travel time", total_travel)

    # TO DO: display mean travel time
    mean_time = selected_file['Trip Duration'].mean()
    print("mean travel time", mean_time )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(selected_file):
    """Displays statistics on bikeshare users."""

   
    start_time = time.time()
    print('\nCalculating User Stats...\n')
    
    # TO DO: Display counts of user types
    print("Counts of user types:\n")

    user_counts = selected_file['User Type'].value_counts()
    
    print(user_counts)

    
    if 'Gender' in selected_file.columns:
       user_stats_gender(selected_file)
    

    if 'Birth Year' in selected_file.columns:
        user_stats_birth(selected_file)

    print("\nThis took %s seconds." % (time.time() - start_time))

def user_stats_gender(selected_file):
    start_time = time.time()
    # TO DO: Display counts of gender
    gender_counts = selected_file['Gender'].value_counts()
    print("Counts of gender:\n")
    
    # iteratively print out the total numbers of genders 
    for index,gender_count   in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))
        print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        
        
    
def user_stats_birth(selected_file):
    """Displays statistics of analysis based on the birth years of bikeshare users."""
    start_time = time.time()
    # Display earliest, most recent, and most common year of birth
    

    # the most earliest birth year
    earliest_year = selected_file['Birth Year'].min()
    print("The most earliest birth year:", earliest_year)
        # the most recent birth year
    most_recent = selected_file['Birth Year'].max()
    print("The most recent birth year:", most_recent)
         # the most common birth year
    most_common_year = selected_file['Birth Year'].mode()[0]
    print("The most common birth year:", most_common_year)
    
    
    
        
    """Displays statistics of analysis based on the birth years of bikeshare users."""
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day, selected_filter = get_filter()
        selected_file = load_data(city, month, day, selected_filter)
        time_stats(selected_file, month, day)
        station_stats(selected_file)
        trip_duration_stats(selected_file)
        user_stats(selected_file)
        user_stats_gender(selected_file)
        user_stats_birth(selected_file)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
