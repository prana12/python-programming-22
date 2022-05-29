hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
weekday = input("Day of the week: ")

if weekday == "Sunday":
    # The salary is double on Sundays
    hourly_wage *= 2

total_wage = hourly_wage * hours_worked
print(f"Daily wages: {total_wage} euros")