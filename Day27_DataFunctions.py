from datetime import datetime

def is_leap_year(year):
    """Check if a year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_year):
    """Calculate age based on current year"""
    current_year = datetime.now().year
    return current_year - birth_year

# --- Input from user ---
year_input = int(input("Enter a year to check if it's a leap year: "))
birth_year = int(input("Enter your birth year to calculate age: "))

# --- Output results ---
print(f"\nLeap Year Check: {year_input} is a leap year? {'Yes' if is_leap_year(year_input) else 'No'}")
print(f"Your age (as of {datetime.now().year}): {calculate_age(birth_year)} years")
