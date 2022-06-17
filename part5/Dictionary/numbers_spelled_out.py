def dict_of_numbers():
    result = {}

    ZERO_TO_NINETEEN = {
        0: 'zero', 
        1: 'one', 
        2: 'two', 
        3: 'three', 
        4: 'four', 
        5: 'five', 
        6: 'six', 
        7: 'seven', 
        8: 'eight', 
        9: 'nine', 
        10: 'ten',
        11: 'eleven', 
        12: 'twelve', 
        13: 'thirteen', 
        14: 'fourteen', 
        15: 'fifteen', 
        16: 'sixteen', 
        17: 'seventeen', 
        18: 'eighteen', 
        19: 'nineteen'
    }

    TENS = {
        20: 'twenty', 
        30: 'thirty', 
        40: 'forty', 
        50: 'fifty', 
        60: 'sixty', 
        70: 'seventy', 
        80: 'eighty', 
        90: 'ninety'
    }

    for n in range(0, 100):
        if n < 20:
            result[n] = ZERO_TO_NINETEEN[n]
        elif n < 100 and n % 10 == 0:
            result[n] = TENS[n]
        else:
            result[n] = TENS[(n - (n % 10))] + '-' + ZERO_TO_NINETEEN[(n % 10)]

    #print(result)
    return result

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])