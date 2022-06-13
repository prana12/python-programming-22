def palindromes():
    while True:
        check = True

        str = input("Please type in a palindrome: ")
        # Run loop from 0 to len/2
        for i in range(0, int(len(str)/2)):
            if str[i] != str[len(str)-i-1]:
                check = False
                
        if check:
            print(f"{str} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")


if __name__ == "__main__":
    palindromes()