import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

FILE = "expenses.csv"


if not os.path.exists(FILE) or os.stat(FILE).st_size == 0:
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])



def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, desc])

    print("Expense added successfully!")



def monthly_summary():
    data = defaultdict(float)

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            month = row["Date"][:7]  
            data[month] += float(row["Amount"])

    print("\n Monthly Summary:")
    for m, amt in data.items():
        print(m, ":", amt)


def analyze():
    data = defaultdict(float)

    
    month_input = input("Enter month (YYYY-MM) for analysis: ")

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            month = row["Date"][:7]

            
            if month == month_input:
                data[row["Category"]] += float(row["Amount"])

    if not data:
        print(" No data found for this month!")
        return

    total = sum(data.values())

    print(f"\n Spending for {month_input}:")
    for k, v in data.items():
        print(k, ":", v)

   
    print("\n Suggestions:")
    for k, v in data.items():
        percent = (v / total) * 100

        if percent > 40:
            print(" Too much spending on", k)
        elif percent > 25:
            print(" Try to control", k)

    # Highest category
    max_cat = max(data, key=data.get)
    print("\n Highest Spending Category:", max_cat)

    #  Pie Chart
    plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%")
    plt.title(f"Expense Distribution for {month_input}")
    plt.show()

    plt.bar(data.keys(), data.values())
    plt.title(f"Expense Distribution for {month_input}")        
    plt.xlabel("Category")
    plt.ylabel("Amount")            
    plt.show()
 



def main():
    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. Analyze Monthly Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_expense()
        elif ch == "2":
            analyze()
        elif ch == "3":
            monthly_summary()
        elif ch == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


main()