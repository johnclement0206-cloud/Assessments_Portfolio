def days_in_month():
    # dictionary mapping month numbers to month names and days
    months_info = {
        1: {"name": "January", "days": 31},
        2: {"name": "February", "days": 28},  # not considering leap years
        3: {"name": "March", "days": 31},
        4: {"name": "April", "days": 30},
        5: {"name": "May", "days": 31},
        6: {"name": "June", "days": 30},
        7: {"name": "July", "days": 31},
        8: {"name": "August", "days": 31},
        9: {"name": "September", "days": 30},
        10: {"name": "October", "days": 31},
        11: {"name": "November", "days": 30},
        12: {"name": "December", "days": 31}
    }

    
    # get month number from user, with input validation checks
    try:
        month_num = int(input("Enter a month number (1-12): "))
        
        # check if month number is valid
        if 1 <= month_num <= 12:
            month_name = months_info[month_num]["name"]
            days = months_info[month_num]["days"]
            print(f"\n{month_name} (Month #{month_num}) has {days} days.")
        else:
            print("Invalid month number! Please enter a number between 1 and 12.")
    
    # source: https://docs.python.org/3/library/exceptions.html#ValueError
    except ValueError:
        print("Invalid input! Please enter a numeric value (1-12).")

# run the program
if __name__ == "__main__":
    days_in_month()