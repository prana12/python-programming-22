yearInput = input("Year: ")
yearInt = int(yearInput)


while True:
    yearInt += 1

    if yearInt % 4 == 0:
        print(f"The next leap year after {yearInput} is {yearInt}")
        break