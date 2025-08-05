def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def pounds_to_kg(pounds):
    return pounds * 0.45359237

def kg_to_pounds(kg):
    return kg / 0.45359237

# --- Sample Usage ---
print("Unit Conversion Examples:\n")

# Length
feet = float(input("Enter value in feet: "))
print(f"{feet} feet = {feet_to_meters(feet):.2f} meters")

meters = float(input("Enter value in meters: "))
print(f"{meters} meters = {meters_to_feet(meters):.2f} feet")

# Weight
pounds = float(input("\nEnter value in pounds: "))
print(f"{pounds} pounds = {pounds_to_kg(pounds):.2f} kilograms")

kg = float(input("Enter value in kilograms: "))
print(f"{kg} kilograms = {kg_to_pounds(kg):.2f} pounds")
