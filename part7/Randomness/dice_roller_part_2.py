from random import choice

def play(die1: str, die2: str, times: int):
    dice = {"A": [3, 6], "B": [2, 5], "C": [1, 4]}
    die1_wins = 0
    die2_wins = 0
    draws = 0
    count = 0

    while count < times:
        count += 1
        die1_score = choice(dice[die1])
        die2_score = choice(dice[die2])
        if die1_score > die2_score:
            die1_wins += 1
        elif die1_score < die2_score:
            die2_wins += 1
        else:
            draws += 1

    return (die1_wins, die2_wins, draws)

if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)