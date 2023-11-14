# stormdecider.py
# @attr: rightside124
# @author: strawberrymaster
# @note: this is a rough draft and doesn't have all the features we need yet

import random

def get_wind_speed(dissipation_type, activity):
    wind_speeds = {
        "TD": [30, 35],
        "TS": [40, 45, 50, 60, 65, 70],
        "C1": [75, 80, 85, 90],
        "C2": [100, 105, 110],
        "C3": [115, 120, 125],
        "C4": [130, 140, 145, 150, 155],
        "C5": {
            "inactive": [160],
            "normal": [160, 165, 175],
            "active": [160, 165, 175, 180, 185, 190, 195, 200, 205, 215],
            "hyperactive": [160, 165, 175, 180, 185, 190, 195, 200, 205, 215, 220, 225]
        }
    }
    if dissipation_type == "C5":
        return random.choice(wind_speeds[dissipation_type][activity])
    else:
        return random.choice(wind_speeds[dissipation_type])

def get_num_storms(activity):
    num_storms = {
        "inactive": [9, 10, 11, 12, 13],
        "normal": [14, 15, 16, 17],
        "active": [18, 19, 20, 21, 22, 23, 24],
        "hyperactive": [25, 26, 27, 28, 29, 30]
    }
    return random.choice(num_storms[activity])

def get_forming_day(season_part):
    forming_days = {
        "Early": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "Mid": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "Late": {
            "Feb": {
                "Normal": [20, 21, 22, 23, 24, 25, 26, 27, 28],
                "Leap": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
            },
            "Apr": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            "Jun": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            "Sep": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            "Nov": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            "Other": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        }
    }
    if season_part == "Late":
        if month == "Feb":
            return random.choice(forming_days[season_part][month][year_type])
        elif month in ["Apr", "Jun", "Sep", "Nov"]:
            return random.choice(forming_days[season_part][month])
        else:
            return random.choice(forming_days[season_part]["Other"])
    else:
        return random.choice(forming_days[season_part])

def is_valid_forming_day(forming_day, month, year_type):
    if forming_day == "31" and month in ["Apr", "Jun", "Sep", "Nov"]:
        return False
    elif forming_day == "30" and month == "Feb":
        return False
    elif forming_day == "29" and month == "Feb" and year_type == "Normal":
        return False
    else:
        return True

start = input("Welcome to Storm Decider. Would you like to run the program? (y/n): ")
if start.lower() == "y":
    activity = input("Choose activity level (inactive, normal, active, hyperactive): ")
    num_storms = get_num_storms(activity)

    region = input("Choose region (NATL, SATL, Mediterranean, SPAC, WPAC, EPAC, SePAC, SWIO, NIO): ")
    month = input("Choose month (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ")

    year_type = input("Choose year type (Normal, Leap): ")
    season_part = input("Choose season part (Early, Mid, Late): ")
    forming_day = str(get_forming_day(season_part))
    while not is_valid_forming_day(forming_day, month, year_type):
        forming_day = str(get_forming_day(season_part))

    dissipation_time = input("Choose dissipation time (0z, 6z, 12z, 18z): ")
    dissipation_type = input("Choose dissipation type (TD, TS, C1, C2, C3, C4, C5): ")
    wind_speed = get_wind_speed(dissipation_type, activity)

    landfall_or_fish = input("Choose landfall or fish storm: ")
    storm_name = input("Choose storm name: ")

    print(f"{storm_name} formed on {month} {forming_day}, dissipated at {dissipation_time}, and peaked as a {dissipation_type} and wind speeds of {wind_speed} mph.")
    if landfall_or_fish == "landfall":
        print("Storm made landfall.")
    elif landfall_or_fish == "fish storm":
        print("Storm dissipated over water.")

else:
    print("Exiting program.")