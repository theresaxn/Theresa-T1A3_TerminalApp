import os.path
import colored
import functions
import styling

print(colored.stylize(
    "Welcome to your Expense Tracker application.", styling.greeting
))

functions.add_line_break()

def create_menu():
    print(f"{colored.Fore.deep_sky_blue_4c}Enter 1 to add an expense to the list.")
    print("Enter 2 to remove an expense on the list.")
    print("Enter 3 to view all expenses on the list.")
    print("Enter 4 to search from a $ range on the list.")
    print(f"Enter 5 to exit.{colored.Style.reset}")

    user_choice = input(
        colored.stylize("Please enter your selection: ", styling.input)
    )
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
        functions.add_line_break()
        functions.add_expense(file_name)
    elif choice == "2":
        functions.add_line_break()
        functions.remove_expense(file_name)
    elif choice == "3":
        functions.add_line_break()
        functions.view_expense(file_name)
    elif choice == "4":
        functions.add_line_break()
        functions.search_expense(file_name)
    elif choice == "5":
        print(colored.stylize(
            "Thank you for using our Expense Tracker application.", styling.greeting
        ))
        functions.add_line_break()
    else:
        print(colored.stylize(
            "Invalid selection, please try again.", styling.error
        ))
        functions.add_line_break()

