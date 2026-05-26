# Project - Expense Tracker

import json 

try : 

    with open("expenses.json", "r") as file:
        expenses = json.load(file)

except FileNotFoundError:
     expenses = []


def save_expenses():
     
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def add_expenses():

    category = input("Enter category : ")
    amount = float(input("Enter amount : "))
    description = input("Enter description : ")

    expense = {
        "category" : category,
        "amount" : amount,
        "description" : description
    }

    expenses.append(expense)
    save_expenses()
     
    print("Expenses saved successfully\n")

def show_expenses():

    if len(expenses) == 0:
        print("Empty expenses")

    else:

        for i, exp in enumerate(expenses):
            print(f"{i + 1}. Category : {exp['category']} | Amount : {exp['amount']} | Description : {exp['description']}\n")

def delete_expenses():

    if len(expenses) == 0:
        print("No expenses to delete\n")

    else:

        show_expenses()

        try:

            index = int(input("Enter the index you want to delete : "))

            if 0 <= index and index < len(expenses):
                expenses.pop(index)
                save_expenses()
                print("Index deleted successfully\n")

            else:
                print("Invalid index\n")

        except ValueError:
            print("Please enter a valid index\n")


def total_expenses():

    total = 0 

    for exp in expenses:
        total += exp['amount']

    print(f"Total expenses : {total}\n")


while True :

    print("===== Expenses Tracker ======")
    print("1. add expenses")
    print("2. show expenses")
    print("3. delete expenses")
    print("4. total expenses")
    print("5. Exit")

    choice = input("Enter choice : ").strip()

    if choice == "1":
        add_expenses()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        delete_expenses()

    elif choice == "4":
        total_expenses()

    elif choice == "5":
        print("Exiting....")
        break 

    else:
        print("Enter valid choice\n")







