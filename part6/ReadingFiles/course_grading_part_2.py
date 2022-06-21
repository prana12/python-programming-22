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
            for exercise in parts[1:]:
                exercise_arr.append(int(exercise))
            
            exercises[parts[0]] = exercise_arr

        return exercises

def read_exam_points_data(exam_points_file: str):
    exam_points = {}

    with open(exam_points_file) as new_file:
        for line in new_file:
            exam_points_arr = []
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "opnro":
                continue
            for point in parts[1:]:
                exam_points_arr.append(int(point))
            
            exam_points[parts[0]] = exam_points_arr

        return exam_points
    
def exec_pts(exercises: list):
    exercise_point = 0

    exercises_total = 0
    for exercise in exercises:
        exercises_total += exercise
    
    if exercises_total == 40:
        exercise_point = 10
    elif exercises_total >= 36 :
        exercise_point = 9
    elif exercises_total >= 32 :
        exercise_point = 8
    elif exercises_total >= 28 :
        exercise_point = 7
    elif exercises_total >= 24 :
        exercise_point = 6
    elif exercises_total >= 20 :
        exercise_point = 5
    elif exercises_total >= 16 :
        exercise_point = 4
    elif exercises_total >= 12 :
        exercise_point = 3
    elif exercises_total >= 8 :
        exercise_point = 2
    elif exercises_total >= 4 :
        exercise_point = 1
    else:
        exercise_point = 0

    return exercise_point

def exm_pts(exam_points: list):
    points = 0

    for point in exam_points:
        points += int(point)

    return points

def determine_grade(total_points: int):
    grade = 0

    if total_points>=0 and total_points<=14:
        grade = 0
    elif total_points>=15 and total_points<=17:
        grade = 1
    elif total_points>=18 and total_points<=20:
        grade = 2
    elif total_points>=21 and total_points<=23:
        grade = 3
    elif total_points>=24 and total_points<=27:
        grade = 4
    elif total_points>=28 and total_points<=30:
        grade = 5
    
    return grade

def show_grades(students: dict, exercises: dict, exam_points: dict):
    for id, name in students.items():
        exercises_point_total = 0
        exam_points_total = 0

        if id in exercises:
            exercises_arr = exercises[id]
            exercises_point_total = exec_pts(exercises_arr)
            
        if id in exam_points:
            exam_points_arr = exam_points[id]
            exam_points_total = exm_pts(exam_points_arr)
            
        print(name[0], name[1], determine_grade(exercises_point_total+exam_points_total))

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
        exam_points = read_exam_points_data(exam_points_file)
        
        show_grades(students, exercises, exam_points)



    