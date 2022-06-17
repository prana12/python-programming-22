def oldest_person(people: list):
    oldest_person = people[0][0]
    oldest_age = people[0][1]

    #my_tuple = (smallest_number, greatest_number, sum_total)
    for i in range(1, len(people)):
        if people[i][1] < oldest_age:
            oldest_person = people[i][0]

    return oldest_person

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))