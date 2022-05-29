times_in_cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
price_of_lunch = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

weekly = groceries + times_in_cafeteria * price_of_lunch

print("Average food expenditure:")
print(f"Daily: {weekly / 7} euros")
print(f"Weekly: {weekly} euros")