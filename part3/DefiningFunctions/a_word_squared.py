def squared(text, times):
    #print((text*(times*times))[0:(times*times)])
    
    looped_text = (text*(times*times))[0:(times*times)]

    count = 0
    while count < times:
        picked_text = looped_text[0:times]
        print(picked_text)
        
        looped_text = looped_text[times:]
        count += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)