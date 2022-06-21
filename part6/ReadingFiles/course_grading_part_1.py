def read_students_info(students_file: str):
    students = {}

    with open(students_file) as new_file:
        for line in new_file:
            #line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            students[parts[0]] = parts[1].strip(), parts[2].strip()

        return students

def read_exercises_info(exercises_file: str):
    exercises = {}

    with open(exercises_file) as new_file:
        for line in new_file:
            exercise_arr = []
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            #exercises[parts[0]] = parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[6]
            for exercise in parts[1:]:
                exercise_arr.append(int(exercise))
            
            exercises[parts[0]] = exercise_arr

        return exercises

def total_number_of_exercises(students: dict, exercises: dict):
    for id, name in students.items():
        if id in exercises:
            exercises_arr = exercises[id]
            total = 0
            for exercise in exercises_arr:
                total += exercise
            print(name[0], name[1], total)

if __name__ == "__main__":
    if False:
        # this is never executed
        students_file = input("Student information: ")
        students = read_students_info(students_file)
        exercises_file = input("Exercises completed: ")
        exercises = read_exercises_info(exercises_file)
    else:
        # hard-coded input
        students_file = "students1.csv"
        exercises_file = "exercises1.csv"
        exam_points_file = "exam_points1.csv"

        students = read_students_info(students_file)
        exercises = read_exercises_info(exercises_file)
        total_number_of_exercises(students, exercises)

    