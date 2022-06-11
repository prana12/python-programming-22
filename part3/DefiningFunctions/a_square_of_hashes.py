def hash_square(number):
    output = ""
    count = 0

    while count < number:
        output += "#"*number + "\n"
        count += 1

    print(output)

if __name__ == "__main__":
    hash_square(3)
    print()
    hash_square(5)