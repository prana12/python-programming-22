def box_of_hashes(size):
    output = ""
    count = 0

    while count < size:
        output += "#"*10 + "\n"
        count += 1

    print(output)

if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)