import datetime

name = input("What is your name? ")
birth_year = input("What is your birth year? ")
current_year = datetime.datetime.now().year

age = current_year - int(birth_year)

lines = [
    f"Welcome, {name}!",
    f"You are {age} years old.",
]

width = max( len(line) for line in lines )

print("┌" + "─" * (width+2) + "┐")
for line in lines:
    print("│ " + line.ljust(width) + " │")
print("└" + "─" * (width+2) + "┘")
