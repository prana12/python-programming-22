from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    #print(f"{amount} - {lower} - {upper}")
    result = []
    included = []

    for i in range(amount):
        while True:
            num = randint(lower, upper)
            if num not in included:
                included.append(num)
                result.append(num)
                break

    return sorted(result)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)