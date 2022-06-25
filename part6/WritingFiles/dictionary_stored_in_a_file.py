def dictionary():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        option = int(input("Function: "))

        if option == 1:
            add_entry()
        elif option == 2:
            search_entries()
        if option == 3:
            print("Bye!")
            break

def add_entry():
    key = input("The word in Finnish: ")
    value = input("The word in English: ")

    with open("dictionary.txt", "a") as my_file:
        my_file.write(f"{key} - {value}\n")
    
    print("Dictionary entry added")

def search_entries():
    dictionary = []

    search_term = input("Search term: ")

    with open("dictionary.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split("-")
            key = parts[0].strip()
            value = parts[1].strip()
            
            #if key.find(search_term) >= 0 or value.find(search_term) >= 0:
            found = key.find(search_term) >= 0 or value.find(search_term) >= 0
            if found:
                dictionary.append(line)

        for item in dictionary:
            print(item)

if __name__ == "__main__":
    dictionary()