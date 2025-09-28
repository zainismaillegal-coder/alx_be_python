# finance_calculator.py
# Personal Finance Calculator (no conditionals)
# Monthly savings = income - expenses
# Projected annual savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
annual_base = monthly_savings * 12
projected = annual_base + (annual_base * 0.05)

print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected:.2f}.")
