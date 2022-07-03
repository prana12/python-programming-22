import json

def print_persons(filename: str):
    # JSON
    with open(filename) as my_file:
        data = my_file.read()

    students = json.loads(data)
    #print(students)
    for student in students:
        print(f"{student['name']} {student['age']} years ({' ,'.join(student['hobbies'])})")

if __name__ == "__main__":
    print_persons("students.json")