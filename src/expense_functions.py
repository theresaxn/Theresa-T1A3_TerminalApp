import csv
import datetime

from colored import Fore, Back, Style

def add_line_break():
    print()

def add_expense(file_name):
    try:
        date_input = input(f"{Style.underline}Enter date of expense (DD/MM/YYYY):{Style.reset} ")
        date_expense = datetime.datetime.strptime(date_input,"%d/%m/%Y").strftime("%d-%m-%Y")
        description_input = input(f"{Style.underline}Enter description of expense:{Style.reset} ")
        amount_input = format(float(input(f"{Style.underline}Enter amount of expense:{Style.reset} $")),".2f")

        with open(file_name, "a") as f:
            writer = csv.writer(f)
            writer.writerow([date_expense,description_input,amount_input])

        add_line_break()

        add_another_input = input(f"{Style.underline}Add another expense (Y/N)?{Style.reset} ")
        if add_another_input.lower() == "y":
            add_expense(file_name)
        elif add_another_input.lower() == "n":
            add_line_break()
        else:
            print(f"{Back.red}Invalid response, returning to main menu.{Style.reset}")
            add_line_break()

    except ValueError:
        print(f"{Back.red}Invalid data entered, please try again.{Style.reset}")
        add_expense(file_name)
    except Exception:
        print(f"{Back.red}Unexpected error occurred, returning to main menu.{Style.reset}")

def remove_expense(file_name):
    try:
        line_input = int(input(f"{Style.underline}Enter line number to be deleted:{Style.reset} "))
        expense_lists = []

        with open(file_name,"r") as f:
            reader = csv.reader(f)
            is_exist = False
            for index, row in enumerate(reader):
                if (line_input != index):
                    expense_lists.append(row)
                else:
                    is_exist = True
        if not is_exist:
            add_line_break()
            print(f"{Fore.light_sea_green}Line number does not exist.{Style.reset}")
        with open(file_name,"w") as f:
            writer = csv.writer(f)
            writer.writerows(expense_lists)

        add_line_break()

        remove_another_input = input(f"{Style.underline}Remove another expense (Y/N)?{Style.reset} ")
        if remove_another_input.lower() == "y":
            view_expense(file_name)
            remove_expense(file_name)
        elif remove_another_input.lower() == "n":
            add_line_break()
        else:
            print(f"{Back.red}Invalid response, returning to main menu.{Style.reset}")
            add_line_break()

    except ValueError:
        print(f"{Back.red}Invalid value entered, please try again.{Style.reset}")
        remove_expense(file_name)
    except FileNotFoundError:
        print(f"{Back.red}Expense Tracker file does not exist.{Style.reset}")
    except Exception:
        print(f"{Back.red}Unexpected error occurred, returning to main menu.{Style.reset}")

def view_expense(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
            row_count = 0
            for index, row in enumerate(reader):
                print(f"{Fore.light_sea_green}Line {index+1} - Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}{Style.reset}")
                row_count =+1
        if row_count == 0:
            print("Nothing to view in the Expense Tracker.")

    except FileNotFoundError:
        print(f"{Back.red}Expense Tracker file does not exist.{Style.reset}")
    except Exception:
        print(f"{Back.red}Unexpected error occurred, returning to main menu.{Style.reset}")

    finally:
        add_line_break()

def search_expense(file_name):
    try:
        min_range_input = float(input(f"{Style.underline}Enter minimum amount to search from:{Style.reset} $"))
        max_range_input = float(input(f"{Style.underline}Enter maximum amount to search to:{Style.reset} $"))

        add_line_break()
        
        with open(file_name,"r") as f:
            reader = csv.reader(f)
            reader.__next__()
            row_count = 0
            for row in reader:
                if (min_range_input <= float(row[2]) <= max_range_input):
                    print(f"{Fore.light_sea_green}Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}{Style.reset}")
                    row_count =+ 1
            if row_count == 0:
                print(f"{Fore.light_sea_green}No expenses found within range.{Style.reset}")
        
        add_line_break()

        search_another_input = input(f"{Style.underline}Search another range (Y/N)?{Style.reset} ")
        if search_another_input.lower() == "y":
            search_expense(file_name)
        elif search_another_input.lower() == "n":
            add_line_break()
        else:
            print(f"{Back.red}Invalid response, returning to main menu.{Style.reset}")
            add_line_break()

    except ValueError:
        print(f"{Back.red}Invalid data entered, please try again.{Style.reset}")
        search_expense(file_name)   
    except FileNotFoundError:
        print(f"{Back.red}Expense Tracker file does not exist.{Style.reset}")
    except Exception:
        print(f"{Back.red}Unexpected error occurred, returning to main menu.{Style.reset}")