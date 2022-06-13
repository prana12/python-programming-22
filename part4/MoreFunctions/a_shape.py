def line(size, character):
    if character == "":
        return ("*"*size)
    else:
        return (character*size)

def shape(size, tri_char, rect_height, rect_char):
    output = ""
    count = 1

    #print triangle
    while count <= size:
        output += line(count, tri_char) + "\n"
        count += 1

    #print square
    count = 1
    while count <= rect_height:
        output += line(size, rect_char) + "\n"
        count += 1

    print(output)

if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")