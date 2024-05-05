import os.path

from colored import Fore, Back, Style

from expense_functions import add_line_break, add_expense, remove_expense, view_expense, search_expense

print(f"{Fore.deep_pink_4c}{Style.bold}Welcome to your Expense Tracker application.{Style.reset}")

add_line_break()

def create_menu():
    print(f"{Fore.deep_sky_blue_4c}Enter 1 to add an expense to the list.")
    print("Enter 2 to remove an expense on the list.")
    print("Enter 3 to view all expenses on the list.")
    print("Enter 4 to search from a $ range on the list.")
    print(f"Enter 5 to exit.{Style.reset}")

    user_choice = input(f"{Style.underline}Please enter your selection:{Style.reset} ")
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
        print(f"{Fore.deep_pink_4c}{Style.bold}Thank you for using our Expense Tracker application.{Style.reset}")
        add_line_break()
    else:
        print(f"{Back.red}Invalid selection, please try again.{Style.reset}")
        add_line_break()

