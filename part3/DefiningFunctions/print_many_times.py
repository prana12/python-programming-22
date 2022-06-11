def print_many_times(text, times):
    counter = 1
    while counter <= times:
        print(text)
        counter += 1

if __name__ == "__main__":
    print_many_times("hi", 5)

    print()

    text = "All Pythons, except one, grow up"
    times = 3
    print_many_times(text, times)