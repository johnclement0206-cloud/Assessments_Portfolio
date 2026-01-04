def counting_loops():
    # 1. Count up from 0 to 50 in increments of 1
    print("\n1. Counting up from 0 to 50 (increment 1):")
    numbers = []
    for i in range(0, 51):
        numbers.append(str(i))
    print(" ".join(numbers))
    
    # 2. Count down from 50 to 0 in decrements of 1
    print("\n2. Counting down from 50 to 0 (decrement 1):")
    numbers = []
    for i in range(50, -1, -1):
        numbers.append(str(i))
    print(" ".join(numbers))
    
    # 3. Count up from 30 to 50 in increments of 1
    print("\n3. Counting up from 30 to 50 (increment 1):")
    numbers = []
    for i in range(30, 51):
        numbers.append(str(i))
    print(" ".join(numbers))
    
    # 4. Count down from 50 to 10 in decrements of 2
    print("\n4. Counting down from 50 to 10 (decrement 2):")
    numbers = []
    for i in range(50, 9, -2):
        numbers.append(str(i))
    print(" ".join(numbers))
    
    # 5. Count up from 100 to 200 in increments of 5
    print("\n5. Counting up from 100 to 200 (increment 5):")
    numbers = []
    for i in range(100, 201, 5):
        numbers.append(str(i))
    print(" ".join(numbers))
    
    print("All counting loops completed.")

# run the program
if __name__ == "__main__":
    counting_loops()
