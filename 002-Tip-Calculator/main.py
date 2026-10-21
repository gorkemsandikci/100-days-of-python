# Day 2 - Tip Calculator
# Topic: Variables, numbers, f-strings

bill = float(input("What is the total bill? "))

tip_percent = float(input("What percentage tip would you like to give? (10 / 15 / 20): "))

people = int(input("How many people to split the bill? "))

tip_amount = bill * tip_percent / 100

total = bill + tip_amount

amount_per_person = total / people

print(f"Each person should pay: ${amount_per_person:.2f}")
