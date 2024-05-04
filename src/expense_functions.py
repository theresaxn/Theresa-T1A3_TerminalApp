import csv
import datetime

def add_line_break():
    print()

def add_expense(file_name):
    try:
        date_input = input("Enter date of expense (DD/MM/YYYY): ")
        date_expense = datetime.datetime.strptime(date_input,"%d/%m/%Y").strftime("%d-%m-%Y")
        description_input = input("Enter description of expense: ")
        amount_input = format(float(input("Enter amount of expense: $")),".2f")
    except ValueError:
        print("Invalid data entered, please try again.")
        add_expense(file_name)
        
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([date_expense,description_input,amount_input])

    add_line_break()

    add_another_input = input("Add another expense (Y/N)? ")
    if add_another_input.lower() == "y":
        add_expense(file_name)
    elif add_another_input.lower() == "n":
        add_line_break()
    else:
        print("Invalid response, back to main menu.")
        add_line_break()
    
def remove_expense(file_name):
    try:
        line_input = int(input("Enter line number to be deleted: "))
        expense_lists = []
    except ValueError:
        print("Invalid value entered, please try again.")
        remove_expense(file_name)
    
    try:
        with open(file_name,"r") as f:
            reader = csv.reader(f)
            is_exist = False
            for index, row in enumerate(reader):
                if (line_input != index):
                    expense_lists.append(row)
                else:
                    is_exist = True
        if not is_exist:
            print("Line number does not exist.")
        with open(file_name,"w") as f:
            writer = csv.writer(f)
            writer.writerows(expense_lists)
    except FileNotFoundError:
        print("Expense Tracker file does not exist.")
        
    add_line_break()

    remove_another_input = input("Remove another expense (Y/N)? ")
    if remove_another_input.lower() == "y":
        view_expense(file_name)
        remove_expense(file_name)
    elif remove_another_input.lower() == "n":
        add_line_break()
    else:
        print("Invalid response, back to main menu.")
        add_line_break()

def view_expense(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
            row_count = 0
            for index, row in enumerate(reader):
                print(f"Line {index+1} - Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}")
                row_count =+1
        if row_count == 0:
            print("Nothing to view in the Expense Tracker.")
    except FileNotFoundError:
        print("Expense Tracker file does not exist.")
    finally:
        add_line_break()

def search_expense(file_name):
    try:
        min_range_input = format(float(input("Enter minimum amount to search from: $")),".2f")
        max_range_input = format(float(input("Enter maximum amount to search to: $")),".2f")
    except ValueError:
        print("Invalid data entered, please try again.")
        search_expense(file_name)
    
    try:
        with open(file_name,"r") as f:
            reader = csv.reader(f)
            reader.__next__()
            row_count = 0
            for row in reader:
                if (float(min_range_input) <= float(row[2]) <= float(max_range_input)):
                    print(f"Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}")
                    row_count =+ 1
            if row_count == 0:
                print("No expenses found within range.")      
    except FileNotFoundError:
        print("Expense Tracker file does not exist.")
    finally:
        add_line_break()