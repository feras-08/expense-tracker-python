from datetime import datetime

def main():

    while True:
        print("\n===== Expenses Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Search by Category")
        print("7. Monthly Summary")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expense()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            search_by_category()

        elif choice == "7":
            monthly_summary()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid choice.")

def add_expense():

    print(" Type 'cancel' to return to menu.")

    category = input("Enter category: ").lower()
    if category.lower() == "cancel":
        return

    while True:
        amount_input = input("Enter amount: ")
        if amount_input.lower() == "cancel":
            return

        try:
            amount = float(amount_input)

            if amount <=0:
                print("Amount must be greater than 0")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    file = open("expenses.txt", "a")
    date = datetime.now().strftime("%m/%d/%Y")
    file.write(date + "," + category + "," + str(amount) + "\n")

    file.close()

    print("Expense added successfully!")

def view_expense():

    try:
        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        expenses = []

        for line in data:
            line = line.strip()

            if line == "":
                continue

            expense = line.split(",")

            if len(expense) == 3:
                expenses.append(expense)

        if len(expenses) == 0:
            print("No expenses found")
            return

        print("\n========== Expenses ==========")
        print("{:<5} {:<15} {:<15} {:<10}".format("No.", "Date", "Category", "Amount"))
        print("-" * 55)

        for index, expense in enumerate(expenses):
            print(
                "{:<5} {:<15} {:<15} $ {:.2f}".format(
                    index + 1,
                    expense[0],
                    expense[1],
                    float(expense[2])
                )
            )

    except FileNotFoundError:
        print("No expenses found")


def total_expenses():

    total = 0

    try:

        file = open("expenses.txt", "r")
        data = file.readlines()

        file.close()

        for line in data:
            expense = line.strip().split(",")

            total += float(expense[2])

        print("\n Total Expenses:" , total)

    except FileNotFoundError:
        print("No expenses found")

def category_summary():
    summary = {}

    try:
        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()
        for line in data:
            expense = line.strip().split(",")

            category = expense[1]
            amount = float(expense[2])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        print("\n ====== Category Summary ======")

        for category, total in summary.items():
            print(category + ": $", total)
    except FileNotFoundError:
        print("No expenses found")


def delete_expense():

    try:
        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        expenses = []

        for line in data:
            if line.strip() != "":
                expense = line.strip().split(",")

                if len(expense) == 3:
                    expenses.append(line)

        if len(expenses) == 0:
            print("No expenses found")
            return

        print("\n===== Delete Expense =====")

        for index, line in enumerate(expenses):
            expense = line.strip().split(",")

            print(str(index + 1) + ". Date:", expense[0])
            print("   Category:", expense[1])
            print("   Amount:", expense[2])
            print("------------------------")

        print("Type 'cancel' to return to menu")

        while True:
            choice = input("Enter expense number to delete: ")

            if choice.lower() == "cancel":
                return

            try:
                choice = int(choice)

                if choice < 1 or choice > len(expenses):
                    print("Invalid expense number")
                else:
                    expenses.pop(choice - 1)

                    file = open("expenses.txt", "w")
                    file.writelines(expenses)
                    file.close()

                    print("Expense deleted successfully!")
                    return

            except ValueError:
                print("Please enter a valid number")

    except FileNotFoundError:
        print("No expenses found")


def search_by_category():
    search = input("Enter category to search: ").lower()

    if search == "cancel":
        return

    try:
        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        found = False

        print("\n===== Search Results =====")
        print("{:<5} {:<15} {:<15} {:<10}".format("No.", "Date", "Category", "Amount"))
        print("-" * 55)

        count = 1

        for line in data:
            line = line.strip()

            if line == "":
                continue

            expense = line.split(",")

            if len(expense) == 3 and expense[1].lower() == search:
                print(
                    "{:<5} {:<15} {:<15} $ {:.2f}".format(
                        count,
                        expense[0],
                        expense[1],
                        float(expense[2])
                    )
                )

                found = True
                count += 1

        if found == False:
            print("No expenses found for this category:", search)
    except FileNotFoundError:
        print("No expenses found")


def monthly_summary():
    month = input("Enter month number (1-12): ")

    if month.lower() == "cancel":
        return

    try:
        month = int(month)

        if month < 1 or month > 12:
            print("Invalid month number")
            return

        file = open("expenses.txt", "r")
        data = file.readlines()
        file.close()

        total = 0

        for line in data:
            line = line.strip()

            if line == "":
                continue

            expense = line.split(",")

            if len(expense) == 3:
                data = expense[0]
                amount = float(expense[2])

                expense_month = int(data.split("/")[0])

                if expense_month == month:
                    total += amount

        print("Total expenses for month", month, "Is $", format(total,".2f"))

    except ValueError:
        print("Please enter a valid month.")

main()

















