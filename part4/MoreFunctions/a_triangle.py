def triangle(size):
    output = ""
    count = 1

    while count <= size:
        output += "#"*count + "\n"
        count += 1

    print(output)

if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)