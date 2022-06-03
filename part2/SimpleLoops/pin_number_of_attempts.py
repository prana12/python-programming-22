attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "4321":
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break

    # this is printed if the code was incorrect
    print("Wrong")