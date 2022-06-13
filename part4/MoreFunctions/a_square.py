def square(size, charater):
    output = ""
    count = 0

    while count < size:
        output += charater*size + "\n"
        count += 1

    print(output)

if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")