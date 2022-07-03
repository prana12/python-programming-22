import csv
import json

def test():

    # CSV
    with open("test.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            print(line)

    # JSON
    with open("courses.json") as my_file:
        data = my_file.read()

    courses = json.loads(data)
    #print(courses)
    for course in courses:
        print(course["name"])

if __name__ == "__main__":
    test()