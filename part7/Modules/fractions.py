from fractions import Fraction

# Import Error happening
def fractionate(amount: int):
    fractions = []

    for i in range(1,amount+1):
        #print(Fraction(3,5))
        print(Fraction(1, amount))
        fractions.append(Fraction(1, amount))

    return fractions

if __name__ == "__main__":
    print(fractionate(5))