def filter_incorrect():
    lottery_numbers = read_entries()
    write_correct_entries(lottery_numbers)

def read_entries():
    lottery_numbers = {}

    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            lottery_numbers[parts[0]] = parts[1]
            
    return lottery_numbers

def write_correct_entries(lottery_numbers: dict):
    correct_entries = ""
    
    for key, value in lottery_numbers.items():
        saved_numbers = []

        try:
            # The week number is incorrect:
            week = int(key.split(" ")[1])

            numbers = value.split(",")
            # Too few numbers:
            if len(numbers) < 7:
                raise ValueError("Too few numbers")

            for item in numbers:
                # One or more numbers are not correct:
                number = int(item)

                # The numbers are too small or large:
                if number < 1 or number > 39:
                    raise ValueError("The numbers are too small or large:")

                # The same number appears twice:
                if number in saved_numbers:
                    raise ValueError("The same number appears twice:")
                
                saved_numbers.append(number)

            #print(f"saved_numbers={saved_numbers}")
            correct_entries += f"{key};{value}\n"
    
        except ValueError:
            #print("ValueError")
            pass # this command doesn't actually do anything

    #print(correct_entries)
    with open("correct_numbers.csv", "w") as my_file:
        my_file.write(f"{correct_entries}")

if __name__ == "__main__":
    filter_incorrect()
    