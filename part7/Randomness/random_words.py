def words(n: int, beginning: str):
    result = []
    found = []

    with open("words.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            
            if parts[0].startswith(beginning):
                if parts[0] not in found:
                    result.append(parts[0])
                    found.append(parts[0])
    
    #print(f"result={result}, len(result)={len(result)}")

    if len(result) >= n:
        result = result[:n]
    else:
        raise ValueError("Not enough words...")

    return result

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)