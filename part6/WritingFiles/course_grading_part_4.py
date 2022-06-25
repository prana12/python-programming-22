def read_students_info(students_file: str):
    students = {}

    with open(students_file) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            students[parts[0]] = parts[1] +  " " + parts[2]

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
    
def read_course_info(course_file: str):
    course = {}

    with open(course_file) as new_file:
        info = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(":")
            info.append(parts[1].strip())
            
        course[info[0]] = info[1]
        #print(course)
    
    return course

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

def prepare_statistics(students: dict, exercises: dict, exam_points: dict):
    statistics_info = (f'{"name":38}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n')
    for id, name in students.items():
        exercises_total = 0
        exercises_point_total = 0
        exam_points_total = 0

        if id in exercises:
            exercises_arr = exercises[id]
            exercises_total = sum(exercises_arr)
            exercises_point_total = exec_pts(exercises_arr)
            
        if id in exam_points:
            exam_points_arr = exam_points[id]
            exam_points_total = exm_pts(exam_points_arr)
            
        total_points = exercises_point_total + exam_points_total
        grade = determine_grade(total_points)
        statistics_info += (f"{name:30}{exercises_total:10}{exercises_point_total:10}{exam_points_total:10}{total_points:10}{grade:10}\n")

    return statistics_info

def writeToCsvFile(students: dict, exercises: dict, exam_points: dict):
    entry = ""
    
    for id, name in students.items():
        entry += f"{id};{name};"
        exercises_point_total = 0
        exam_points_total = 0

        if id in exercises:
            exercises_arr = exercises[id]
            exercises_point_total = exec_pts(exercises_arr)
            
        if id in exam_points:
            exam_points_arr = exam_points[id]
            exam_points_total = exm_pts(exam_points_arr)
            
        total_points = exercises_point_total + exam_points_total
        grade = determine_grade(total_points)
        entry += f"{grade}\n"

    #print(entry)
    with open("results.csv", "w") as my_file:
        my_file.write(entry)

def writeToTextFile(course: dict, students: dict, exercises: dict, exam_points: dict):
    entry = ""

    for name, credits in course.items():
        entry += f"{name}, {credits} credits\n"
    entry += f"======================================\n"
    
    statistics_info = prepare_statistics(students, exercises, exam_points)
    entry += statistics_info

    #print(entry)
    with open("results.txt", "w") as my_file:
        my_file.write(entry)

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
        course_file = "course1.txt"

        students = read_students_info(students_file)
        exercises = read_exercises_info(exercises_file)
        exam_points = read_exam_points_data(exam_points_file)
        course_info = read_course_info(course_file)
        
        #writing exercise
        writeToTextFile(course_info, students, exercises, exam_points)
        writeToCsvFile(students, exercises, exam_points)


        



    