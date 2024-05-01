print("Welcome to your Expense Tracker application.")

def create_menu():
    print("1. Enter 1 to add an expense to the list.")
    print("2. Enter 2 to remove an expense on the list.")
    print("3. Enter 3 to view all expenses on the list.")
    print("4. Enter 4 to search from a $ range on the list.")
    print("5. Enter 5 to exit.")

    user_choice = input("Enter your selection: ")
    return user_choice

choice = ""

while choice != "5":
    choice = create_menu()

    if choice == "1":
        pass
    if choice == "2":
        pass
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice == "5":
        pass
    else:
        print("Invalid selection, please try again.")

print("Thank you for using the Expense Tracker application.")