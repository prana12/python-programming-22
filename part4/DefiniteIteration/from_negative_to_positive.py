def negative_to_positive():
    positive = int(input("Please type in a positive integer: "))

    for i in range(-positive, positive+1, 1):
        if i != 0:
            print(i)


if __name__ == "__main__":
    negative_to_positive()