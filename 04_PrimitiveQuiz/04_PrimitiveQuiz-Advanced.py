def european_capitals_quiz():
    countries_capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London",
        "Netherlands": "Amsterdam",
        "Poland": "Warsaw",
        "Sweden": "Stockholm",
        "Portugal": "Lisbon",
        "Greece": "Athens"
    }
    
    # create empty var "score" to track score
    score = 0
    total_questions = len(countries_capitals)
    
    print("=== European Capitals Quiz ===")
    print(f"Answer the capitals for {total_questions} European countries.\n")
    
    # loop through each country
    for country, correct_capital in countries_capitals.items():
        # ask the question
        user_answer = input(f"What is the capital of {country}? ")
        
        # check answer (case-insensitive using strip() and lower() func)
        ### sources: https://docs.python.org/3/library/stdtypes.html#str.strip
        #            https://docs.python.org/3/library/stdtypes.html#str.lower
        if user_answer.strip().lower() == correct_capital.lower():
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The capital of {country} is {correct_capital}.")
        
        print()  # blank line for readability
    
    # display final score
    print(f"Quiz completed!")
    print(f"Your score: {score}/{total_questions}")
    
    # calculate percentage
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # provide feedback based on score
    if percentage >= 90:
        print("Excellent! You know your European capitals!")
    elif percentage >= 70:
        print("Good job! You know most European capitals.")
    elif percentage >= 50:
        print("Not bad! You know some European capitals.")
    else:
        print("Keep studying! You'll learn more with practice.")

# run the quiz
if __name__ == "__main__":
    european_capitals_quiz()
