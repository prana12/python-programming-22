number = int(input("Please type in a number: "))

# Sample 1
""" x = 0
count = 1
output = ""

while x < number:
    print(f"x = {x}")
    #print(count + x)
    #print(number - x)
    if str(count + x) in output:
        break
    else:
        output += str(count + x) + "\n"
    
    if str(number - x) in output:
        break
    else:
        output += str(number - x) + "\n"

    x += 1

print(output) """


# Sample 1
count = 1
output = ""
max = number+1

while count <= max:
    #print(f"count = {count}")

    if str(count) in output:
        break
    else:
        #print(f"PLUS: {count}")
        output += str(count) + "\n"
    
    if str(max - count) in output:
        break
    else:
        #print(f"MINUS: {max - count}")
        output += str(max - count) + "\n"

    count += 1

print(output)