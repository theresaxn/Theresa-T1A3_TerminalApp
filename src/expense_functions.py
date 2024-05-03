import csv
import datetime

def add_expense(file_name):
    try:
        date_input = input("Enter date of expense (DD/MM/YYYY): ")
        date_expense = datetime.datetime.strptime(date_input,"%d/%m/%Y").strftime("%d-%m-%Y")
    except ValueError:
        print(f"Invalid date, please try again.")
        date_input = input("Enter date of expense (DD/MM/YYYY): ")
    description_input = input("Enter description of expense: ")
    amount_input = format(float(input("Enter amount of expense: $")),".2f")
    
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([date_expense,description_input,amount_input])

def remove_expense(file_name):
    pass

def view_expense(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
            for index, row in enumerate(reader):
                print(f"{index+1}. Date: {row[0]}, Description: {row[1]}, Amount: ${row[2]}")
    except FileNotFoundError:
        print("Expense Tracker file does not exist.")
    except ValueError:
        print("Nothing to view in Expense Tracker.")

def search_expense(file_name):
    pass