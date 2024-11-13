import json
import datetime

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    global transactions
    try: # place the code that can trow error
        with open("transactions.json", "r") as file: # Open the JSON file in read mode
            return json.load(file) # Load transactions from the user
    except FileNotFoundError: # If the file is not found
        return[] # Return epty list
        

def save_transactions():
    with open("transactions.json", "w") as file: # Open the JSON file in write mode
        json.dump(transactions,file) # Write transactions to the file

# Feature implementations
def add_transaction():
    while True:
        try:
            amount = float(input("\nEnter the amount of transaction : "))
        except ValueError: # To handle error
            print("Your Input is Incorrect. Please Enter a Numeric Value.\n")
        else:
            break

                    
    while True:
        category = input("Enter the category(Salary, Food, Transport, Healthcare, Housing, Other) :") # Prompt for input from user
        if category == "Salary" or category == "salary" or category == "SALARY" or category == "Food" or category == "food" or category == "FOOD" or category == "Housing" or category == "housing" or category == "HOUSING" or category == "Healthcare" or category == "healthcare" or category == "HEALTHCARE" or category =="Other" or category == "other" or category == "OTHER" or category == "Transport" or category == "TRANSPORT" or category == "transport":
        # User can enter a category one of above category
            break
        else:
            print("Invalid category!\nPlease Enter the one of given category.\n") # If user input out of range category diplay this


    while True:
        type_transaction = input("Enter the type of transaction(income / expense) : ")
        if type_transaction  == "income" or type_transaction =="expense" :
            break
        else:
            print("Invalid input!\nPlease Enter the given type of transaction.\n")
    today = datetime.datetime.now().date()
    date = str(today)
    print(date)

   
    global transactions
    transactions.append( [ amount, category, type_transaction, date])# Append new data
    save_transactions() # To save the new data
    print("The transaction added successfully!") 
    
            
          
    
def view_transactions():
    global transactions
    if transactions:
            number = 1
            for trans in transactions:
                print(f"{number}) {trans}")
                number += 1
    else:
        print("No transactions found.")

def update_transaction():
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating
    #index = int("Enter the index of you want to change transaction : ")

    global transactions
    if not transactions:
        print("No any transaction to update.")
        return

    view_transactions()
    try:
        while True:
            try:
                number = int(input("Enter the index of the transaction you want to update: ")) 
                if 0 <= number < len(transactions):
                    transaction = transactions[number]
                while True:
            # Prompt user for new transaction details
            # Update the transaction in the transactions list
            # Save transactions to the file
                    try:
                        new_amount = float(input("\nEnter the new amount of transaction : "))
            # If invalid, print an error message
                    except ValueError:
                        print("Your Input is Incorrect. Please Enter a Numeric Value.\n")
                    else:
                        break
                            
                while True:
                    new_category = input("Enter the new category(Salary, Food, Transport, Healthcare, Housing, Other) :")
                    if new_category == "Salary" or new_category == "salary" or new_category == "SALARY" or new_category == "Food" or new_category == "food" or new_category == "FOOD" or new_category == "Housing" or new_category == "housing" or new_category == "HOUSING" or new_category == "Healthcare" or new_category == "healthcare" or new_category == "HEALTHCARE" or new_category =="Other" or new_category == "other" or new_category == "OTHER" or new_category == "Transport" or new_category == "TRANSPORT" or new_category == "transport":
                        break
                    else:
                        print("Invalid category!\nPlease Enter the one of given category.\n")


                while True:
                    new_type_transaction = input("Enter the new type of transaction(income / expense) : ")
                    if new_type_transaction == "income" or new_type_transaction == "expense" :
                        break
                    else:
                        print("Invalid input!\nPlease Enter the given type of transaction.\n")
                        
                    new_today = datetime.datetime.now().date()
                    new_date = str(new_today)

                else:
                    print("You entered out of range number. Please check the number you entered.")

            except ValueError:
                print("Invalid input. Please enter a numeric number.")




        transactions[number] = { new_amount, new_category, new_type_transaction, today, new_today}
        save_transactions()
        print("The new transaction updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

    
def delete_transaction():
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting
    global transactions
    if not transactions:
        print("No transactions available to delete.")
        return

    view_transactions()
    try:
        index = int(input("Enter the index of the transaction you want to delete: ")) - 1
        if 0 <= index < len(transactions):
            del transactions[index]
            save_transactions() # Save transactions to the file
            print("Transaction deleted successfully!") 
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.") # Print a success message
        # If invalid, print an error message
    # If no transactions exist, print a message indicating so




def display_summary():
    # Placeholder for summary display logic
    global transactions
    total_income = 0
    total_expense = 0

    for transaction in transactions:  # Check if there are transactions available
        # Calculate total income, total expense, and net income
        if transaction[2].lower() == "income":
            total_income += transaction[0]
        elif transaction[2].lower() == "expense":
            total_expense += transaction[0]

    print("Summary:")
    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Balance:", total_income - total_expense)



def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 
