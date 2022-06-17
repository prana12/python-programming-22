def square_of_letters(number: int):
    alphabets = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z"
    }
    square_length = number + (number-1)
    ts = square_length
    center = (square_length // 2)
    counter=0
    print(center)

    outcome = ""
    for row in range(ts):
        for col in range(ts):
            if row<=center and ts-counter>col:
                outcome+=alphabets[center-min(row,col)]
            elif row <=center and col>=ts-counter :
                outcome+=alphabets[col-center]
            elif row>center and ts-counter>col:
                outcome+=alphabets[center-min(row,col)]
            elif row >center and col<counter :   
                outcome+=alphabets[row-center]
            elif row >center and col>=counter :   
                outcome+=alphabets[row-center+(col-counter)]

        counter=counter+1  
        outcome += "\n"

    return outcome

if __name__ == "__main__":
    square = square_of_letters(2)
    #square = square_of_letters(3)
    print(square)