def diary():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit ")
        option = int(input("Function: "))

        if option == 1:
            add_entry()
        elif option == 2:
            read_entries()
        if option == 0:
            print("Bye now!")
            break


def add_entry():
    entry = input("Diary entry: ")

    with open("diary.txt", "a") as my_file:
        my_file.write(entry + "\n")
    
    print("Diary saved \n")

def read_entries():
    print("Entries: ")

    with open("diary.txt") as new_file:
        for line in new_file:
            print(line, end="")

if __name__ == "__main__":
    diary()
    