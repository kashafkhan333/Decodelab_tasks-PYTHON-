# Expense Tracker Program

expenses = []

print("===== EXPENSE TRACKER =====")

while True:
    amount = input("Enter expense amount (or type 'done' to finish): ")

    if amount.lower() == "done":
        break

    try:
        amount = float(amount)
        expenses.append(amount)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Calculate total expense
total = sum(expenses)

print("\n===== EXPENSE SUMMARY =====")

if len(expenses) == 0:
    print("No expenses were entered.")
else:
    print("Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Rs. {expense}")

    print("---------------------------")
    print(f"Total Expenses: Rs. {total}")
