from random import choice

def roll(die: str):
    dice = {"A": [3, 6], "B": [2, 5], "C": [1, 4]}
    return choice(dice[die])

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")