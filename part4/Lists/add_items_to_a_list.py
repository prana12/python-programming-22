numbers = []

size = int(input("How many items: "))
count = 1

while count <= size:
    value = int(input(f"Item {count}: "))
    numbers.append(value)
    count += 1

print(numbers)