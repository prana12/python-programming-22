def phone_book():
    contacts = {}
    print(contacts)

    while True:
        option = int(input("command (1 search, 2 add, 3 quit):"))
        if option == 1:
            name = input("name: ")

            if name in contacts:
                #print(f"number: {contacts[name]}")
                for number in contacts[name]:
                    print(number)
            else:
                print("no number")

        elif option == 2:
            name = input("name: ")
            number = input("number: ")

            if name not in contacts:
                contacts[name] = []

            contacts[name].append(number)
            print("ok!")

        elif option == 3:
            print("quitting...")
            break

if __name__ == "__main__":
    phone_book()