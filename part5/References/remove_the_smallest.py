def remove_smallest(numbers: list):
    smallest_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i

    numbers.pop(smallest_index)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)