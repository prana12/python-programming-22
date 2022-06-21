def largest():
    numbers = []

    with open("numbers.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            #print(line)
            numbers.append(int(line))
            
    largest = numbers[0]
    for i in numbers[1:]:
        if i >largest:
            largest = i
        
    print(largest)

if __name__ == "__main__":
    largest()