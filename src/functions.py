import csv
import datetime
import colored
import styling

def add_line_break():
    print()

class NegativeError(Exception):
    pass

class RangeError(Exception):
    pass

def add_expense(file_name):
    try:
        date_input = input(
            colored.stylize("Enter date of expense (DD/MM/YYYY): ", styling.input)
        )
        date_expense = datetime.datetime.strptime(date_input,"%d/%m/%Y").strftime("%d-%m-%Y")
        description_input = input(
            colored.stylize("Enter description of expense: ", styling.input)
        )
        amount_input = format(float(input(
                colored.stylize(f"Enter amount of expense: $", styling.input)
        )),".2f")

        if float(amount_input) < 0:
            raise NegativeError

        with open(file_name, "a") as f:
            writer = csv.writer(f)
            writer.writerow([date_expense,description_input,amount_input])

        add_line_break()

    except ValueError:
        print(colored.stylize(
            "Invalid data entered, please try again.", styling.error
        ))
        add_expense(file_name)
    except NegativeError:
        print(colored.stylize(
            "No negative numbers, please try again.", styling.error
        ))
        add_expense(file_name)

def add_another_expense(file_name):
    add_another_input = input(
        colored.stylize("Add another expense (Y/N)? ", styling.input)
    )
    if add_another_input.lower() == "y":
        add_line_break()
        add_expense(file_name)
        add_another_expense(file_name)
    elif add_another_input.lower() == "n":
        add_line_break()
    else:
        print(colored.stylize(
            "Invalid response, returning to main menu.", styling.error
        ))
        add_line_break()

def remove_expense(file_name):
    try:
        view_expense(file_name)
        line_input = int(input(
            colored.stylize("Enter line number to be deleted: ", styling.input)
        ))
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
            print(
                colored.stylize("Line number does not exist.", styling.output)
            )
        with open(file_name,"w") as f:
            writer = csv.writer(f)
            writer.writerows(expense_lists)

        add_line_break()

    except ValueError:
        print(colored.stylize(
            "Invalid value entered, please try again.", styling.error
        ))
        remove_expense(file_name)
    except FileNotFoundError:
        print(colored.stylize(
            "Expense Tracker file does not exist.", styling.error
        ))

def remove_another_expense(file_name):
    remove_another_input = input(
        colored.stylize("Remove another expense (Y/N)? ", styling.input)
    )
    if remove_another_input.lower() == "y":
        remove_expense(file_name)
        remove_another_expense(file_name)
    elif remove_another_input.lower() == "n":
        add_line_break()
    else:
        print(colored.stylize(
            "Invalid response, returning to main menu.", styling.error
        ))
        add_line_break()

def view_expense(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
            row_count = 0
            for index, row in enumerate(reader):
                print(
                    colored.stylize(
                        f"Line {index+1} - Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}",
                        styling.output
                    )
                )
                row_count =+ 1
        if not row_count:
            add_line_break()
            print(colored.stylize(
                    "Nothing to view in the Expense Tracker.", styling.output
            ))

    except FileNotFoundError:
        print(colored.stylize(
            "Expense Tracker file does not exist.", styling.error
        ))

    finally:
        add_line_break()

def search_expense(file_name):
    try:
        min_input = float(input(
        colored.stylize("Enter minimum search amount: $", styling.input)
        ))

        if min_input < 0:
            raise NegativeError
        
        max_input = float(input(
            colored.stylize("Enter maximum search amount: $", styling.input)
        ))

        if max_input < 0:
            raise NegativeError
        
        if min_input > max_input:
            raise RangeError
        
        add_line_break()
        
        with open(file_name,"r") as f:
            reader = csv.reader(f)
            reader.__next__()
            row_count = 0
            for row in reader:
                if (min_input <= float(row[2]) <= max_input):
                    print(colored.stylize(
                            f"Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}", styling.output
                    ))
                    row_count =+ 1
            if not row_count:
                print(colored.stylize(
                    "No expenses found within range.", styling.output
                ))
        
        add_line_break()

    except ValueError:
        print(colored.stylize(
            "Invalid data entered, please try again.", styling.error
        ))
        search_expense(file_name)
    except NegativeError:
        print(colored.stylize(
            "No negative numbers, please try again.", styling.error
        ))
        search_expense(file_name)
    except RangeError:
        print(colored.stylize(
            "Minimum range cannot exceed maximum range search, please try again.",
            styling.error
        ))
        search_expense(file_name) 
    except FileNotFoundError:
        print(colored.stylize(
            "Expense Tracker file does not exist.", styling.error
        ))

def search_another_expense(file_name):
    search_another_input = input(
        colored.stylize("Search another range (Y/N)? ", styling.input)
    )
    if search_another_input.lower() == "y":
        add_line_break()
        search_expense(file_name)
        search_another_expense(file_name)
    elif search_another_input.lower() == "n":
        add_line_break()
    else:
        print(colored.stylize(
            "Invalid response, returning to main menu.", styling.error
        ))
        add_line_break()