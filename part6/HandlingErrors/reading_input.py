def read_input(question: str, min: int, max: int):
    while True:
        try:
            input_str = input(question)
            number = int(input_str)
            if number >= min and number <= max:
                return number
        except ValueError:
            pass # this command doesn't actually do anything

        print(f"You must type in an integer between {min} and {max}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
    