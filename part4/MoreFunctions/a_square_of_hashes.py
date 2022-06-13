def square_of_hashes(size):
    output = ""
    count = 0

    while count < size:
        output += "#"*size + "\n"
        count += 1

    print(output)

if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)