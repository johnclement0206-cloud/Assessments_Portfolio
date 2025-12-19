def basic_search():
    # initialize the list
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    
    # get search term from user
    search_name = input("Enter a name to search for: ")
    
    # search through the list
    found = False
    for name in names:
        if name == search_name:
            found = True
            break
    
    if found:
        print(f"'{search_name}' was found in the list.")
    else:
        print(f"'{search_name}' was not found in the list.")

# run the program
if __name__ == "__main__":
    basic_search()