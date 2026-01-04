def days_in_month_enhanced():
    # dictionary mapping month numbers to month names and days
    months_info = {
        1: {"name": "January", "days": 31},
        2: {"name": "February", "days": 28},  # default value
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
            
            # special handling for February to account for leap years
            if month_num == 2:
                # get year from user to determine leap year automatically
                try:
                    year = int(input("Enter the year (e.g., 2024): "))
                    
                    # check if it's a leap year
                    # leap year rule: divisible by 4, but not by 100 unless also divisible by 400
                    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                    
                    if is_leap_year:
                        days = 29
                        print(f"\n{month_name} (Month #{month_num}) in {year} has {days} days (leap year).")
                    else:
                        print(f"\n{month_name} (Month #{month_num}) in {year} has {days} days.")
                        
                except ValueError:
                    print("Invalid year! Please enter a valid year (e.g., 2024).")
                    # fallback to simple yes/no approach
                    leap_year_response = input("Is it a leap year? (yes/no): ").strip().lower()
                    
                    if leap_year_response in ["yes", "y"]:
                        days = 29
                        print(f"\n{month_name} (Month #{month_num}) has {days} days in a leap year.")
                    elif leap_year_response in ["no", "n"]:
                        print(f"\n{month_name} (Month #{month_num}) has {days} days.")
                    else:
                        print("Invalid response! Assuming it's not a leap year.")
                        print(f"\n{month_name} (Month #{month_num}) has {days} days.")
            else:
                print(f"\n{month_name} (Month #{month_num}) has {days} days.")
        else:
            print("Invalid month number! Please enter a number between 1 and 12.")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value (1-12).")

# run the program
if __name__ == "__main__":
    days_in_month_enhanced()