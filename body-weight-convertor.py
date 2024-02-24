# This program will ask for user body weight in pounds (lbs) and convert it in kilogram (kg)
# It will display 3 digits decimals, e.g. 10.123 kg

weight_lbs = float(input("Enter weight in pounds (lbs): "))
weight_kg = round(weight_lbs/2.2, 3)
print (f"Your body weight is: {weight_lbs} lbs, and the equivalent in kg is: {weight_kg}.\nThank you")