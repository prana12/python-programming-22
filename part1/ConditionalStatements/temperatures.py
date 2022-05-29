temp = int(input("Please type in a temperature (F): "))
temp_in_celsius = (temp - 32) / 1.8000

print(f"{temp} degrees Fahrenheit equals {temp_in_celsius} degrees Celsius")

if temp_in_celsius < 0:
    print(f"Brr! It's cold in here!")