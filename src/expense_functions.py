import csv
import datetime

def add_expense(file_name):
    try:
        date_input = input("Enter date of expense (DD/MM/YYYY): ")
        date_expense = datetime.datetime.strptime(date_input,"%d/%m/%Y").strftime("%d-%m-%Y")
    except ValueError:
        print(f"Invalid date, please try again.")
        date_input = input("Enter date of expense (DD/MM/YYYY): ")


def remove_expense(file_name):
    pass

def view_expense(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
        for row in reader:
            print(f"Date: {row[0]}, Description: {row[1]}, Amount: ${row[-1]}")
    except FileNotFoundError:
        print("Expense Tracker file does not exist.")
    except ValueError:
        print("Nothing to view in Expense Tracker.")

def search_expense(file_name):
    pass