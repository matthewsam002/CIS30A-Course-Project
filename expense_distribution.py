# Input monthly Expenses
# function number 1
def calculate_sum_of_expenses():
    expenses_dict = {}

    # Use of while loop
    while True:
        input_expense = input("Enter expenses in the format 'expense:spent' (or 'f' when finished): ")

        if input_expense.lower() == 'f':
            break

        try:
            key, value = input_expense.split(":")
            value = int(value)
            expenses_dict[key.strip()] = value
        except ValueError:
            print("Invalid input format. Please enter in the format 'string:integer'.")

    total_expenses = sum(expenses_dict.values())

    return "Expense List:", expenses_dict, \
        "Total Expenses: ", total_expenses


