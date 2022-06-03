number = float(input("Please type in a number: "))

intpart = int(number)
#decpart = number - intpart
decpart = round(number - intpart, 2)

print(f"Integer part: {intpart}")
print(f"Decimal part: {decpart}")