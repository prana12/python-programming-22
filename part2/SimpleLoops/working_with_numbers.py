#number = int(input("Number: "))
count = 0
sum = 0
positives = 0
negatives = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {sum/count}")
        print(f"Positive numbers {positives}")
        print(f"Negative numbers {negatives}")
        break
    count += 1
    sum += number
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1