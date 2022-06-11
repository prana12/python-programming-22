def chessboard(size):
    output = ""
    a = 0
    b = 0

    while a < size:
        while b < size:
            #print(f"a: {a}, b: {b}")
            if (a%2==0) == (b%2==0):
                output += "1"
            else:
                output += "0"
            b += 1

        output += "\n"
        b = 0
        a += 1

    print(output)

if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)