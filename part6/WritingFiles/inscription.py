def inscribe():
    name = input("Whom should I sign this to: ")
    file = input("Where shall I save it: ")

    with open(file, "w") as my_file:
        my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

if __name__ == "__main__":
    inscribe()
    