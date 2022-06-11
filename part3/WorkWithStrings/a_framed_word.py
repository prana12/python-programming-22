word = input("Word: ")
mid = len(word)//2
#print(f"{word} mid is {mid}")

width = 30
overall_mid = (width)//2
#print(f"Length mid is {overall_mid}")

start_pos = overall_mid-mid
#print(f"starting pos = {start_pos} AND ending pos = {start_pos+len(word)}")

output = ""

output += "******************************"
output += "\n"

#logic to add word in the middle
count = 1
while count <= width:
    if count == 1 or count == width:
        output += "*"
    elif count >= overall_mid-mid and count < overall_mid-mid+len(word) :
        #print(f"count -> {count}")
        output += word[count-start_pos]
    else:
        output += " "
    count += 1;

output += "\n"
output += "******************************"
print(output)