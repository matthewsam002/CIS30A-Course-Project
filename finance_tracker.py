# Personal Finance Tracking Program
import expense_distribution

# go into another module and get tuple of expenses and the total
expense_info = expense_distribution.calculate_sum_of_expenses()
expense_list = expense_info[:2]
expense_total = expense_info[-1]

class FinanceTracker:
    def __init__(self):
        self.budget = 0
        self.income = 0
        self.savings = 0

    # the total the person wants to spend
    def update_budget(self, budget):
        self.budget = budget

    def update_income(self, income):
        self.income = income

    def update_savings(self, savings):
        self.savings = savings

    # gets the layout for the .txt file
    def calculate_summary(self):
        # savings is what's left over after expenses
        self.savings = self.income - expense_total
        return f"Budget: ${self.budget}\n" \
               f"Income: ${self.income}\n"\
               f"Savings: ${self.savings}\n"\

def main():
    finance_tracker = FinanceTracker()

    try:
        # get input for income and budget
        finance_tracker.update_budget(float(input("Enter your budget: $")))
        finance_tracker.update_income(float(input("Enter your income: $")))

        # Output summary to a text file
        with open("C:\\Users\\mathe\\Downloads\\CIS30_project\\python_project.txt", "w") as f:
            f.write(str(expense_list) + "\n")
            f.write("Expenses: $" + str(expense_total) + "\n")
            f.write(finance_tracker.calculate_summary())
            print("Summary written to 'C:\\Users\\mathe\\Downloads\\CIS30_project\\python_project.txt'.")

    except ValueError:
        print("Error: Please enter valid numeric values for budget, income, expenses, and savings.")

if __name__ == "__main__":
    main()
