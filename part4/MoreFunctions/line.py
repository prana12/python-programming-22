def line(size, text):
    if text == "":
        print("*"*size)
    else:
        print(text[0:1]*size)

if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")