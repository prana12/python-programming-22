from turtle import width


def spruce(size):
    print("a spruce!")

    output = ""
    count = 0
    width = 1

    max_size = (size*2)-1
    mid_index = max_size//2

    while count < size:        
        output += " "*(mid_index-count) + "*"*width + "\n"
        width += 2
        count += 1

    output += " "*(mid_index) + "*" + "\n"
    print(output)
    

if __name__ == "__main__":
    spruce(3)
    #spruce(5)