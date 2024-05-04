import os.path

from expense_functions import add_line_break, add_expense, remove_expense, view_expense, search_expense

print("Welcome to your Expense Tracker application.")

def create_menu():
    print("Enter 1 to add an expense to the list.")
    print("Enter 2 to remove an expense on the list.")
    print("Enter 3 to view all expenses on the list.")
    print("Enter 4 to search from a $ range on the list.")
    print("Enter 5 to exit.")

    user_choice = input("Please enter your selection: ")
    return user_choice

file_name = "expense_tracker.csv"

if (not os.path.isfile(file_name)):
    expense_file = open(file_name, "w")
    expense_file.write("Date,Description,Amount\n")
    expense_file.close()

choice = ""

while choice != "5":
    choice = create_menu()

    if choice == "1":
        add_expense(file_name)
    elif choice == "2":
        remove_expense(file_name)
    elif choice == "3":
        view_expense(file_name)
    elif choice == "4":
        search_expense(file_name)
    elif choice == "5":
        print("Thank you for using our Expense Tracker application.")
    else:
        print("Invalid selection, please try again.")
        add_line_break()