import mysql.connector
from mysql.connector import Error

# Connect to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # replace with your MySQL username
            password='Srinivas@112',   # replace with your MySQL password
            database='ExpenseTracker'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Function to add an expense
def add_expense(connection, amount, category, description, date):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (%s, %s, %s, %s)", 
                       (amount, category, description, date))
        connection.commit()
        print("Expense added successfully.")
    except Error as e:
        print("Error adding expense:", e)

# Function to view expenses
def view_expenses(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        print("ID | Amount | Category | Description | Date")
        print("-------------------------------------------")
        for row in rows:
            print(row)
    except Error as e:
        print("Error retrieving expenses:", e)

# Function to add a category
def add_category(connection, category_name):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO categories (name) VALUES (%s)", (category_name,))
        connection.commit()
        print("Category added successfully.")
    except Error as e:
        print("Error adding category:", e)

# Main program loop
def main():
    connection = connect_to_db()
    if connection is None:
        print("Failed to connect to the database. Exiting...")
        return

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Category")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(connection, amount, category, description, date)
        elif choice == "2":
            view_expenses(connection)
        elif choice == "3":
            category_name = input("Enter new category name: ")
            add_category(connection, category_name)
        elif choice == "4":
            connection.close()
            print("Connection closed. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
