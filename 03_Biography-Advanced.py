print("Please enter your personal information:")

# Get name and hometown
name = input("Enter your full name: ")
hometown = input("Enter your hometown (city and state/country): ")

# get age with error handling
while True:
    age_input = input("Enter your age (numbers only): ")
    
    # check if input is numeric
    if age_input.isdigit():
        age = int(age_input)
        if age > 0 and age < 100:  # reasonable age range check
            break
        else:
            print("Please enter a valid age (1-150).")
    else:
        print("Error: Age must be a number. Please try again.")

personal_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(f"Name: {personal_info['name']}")
print(f"Hometown: {personal_info['hometown']}")
print(f"Age: {personal_info['age']}")