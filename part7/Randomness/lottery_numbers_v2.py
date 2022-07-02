from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    shuffle(number_pool)
    draw = number_pool[0:7]
    return sorted(draw)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)