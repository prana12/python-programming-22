def factorials(n: int):
    results = {}
    fact = 1
    count = 1

    while count <= n:
        fact *= count
        results[count] = fact
        count += 1

    return results

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])