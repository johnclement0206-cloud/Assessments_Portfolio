def password_system():
    # define the correct password
    correct_password = "12345"
    
    # set maximum attempts
    max_attempts = 5
    attempts = 0
    
    print("Password Entry System")
    print("Enter the correct password to continue.")
    print()
    
    while attempts < max_attempts:
        # get password input from user
        user_input = input(f"Attempt {attempts + 1}/{max_attempts}: Enter password: ")
        
        # check if password is correct
        if user_input == correct_password:
            print("Correct password! Access granted.")
            return
        
        # password is incorrect
        attempts += 1
        remaining_attempts = max_attempts - attempts
        
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempt(s) remaining.")
        else:
            print("Incorrect password.")
    
    # maximum attempts reached
    print()
    print("Maximum password attempts reached.")
    print("Authorities have been alerted.")

# run the program
if __name__ == "__main__":
    password_system()
