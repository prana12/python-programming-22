limit = int(input("Upper limit:"))
count = 1
sum = count
summary = f"The consecutive sum: {count}"

while sum < limit:
    count += 1
    sum += count
    summary += f" + {count}"
    
   
    
print(f"{summary} = {sum}")