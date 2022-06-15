def main():
    inputs = input_from_user()
    

# Exam points are integers between 0 and 20. 
# The number of exercises completed is an integer between 0 and 100.
def input_from_user():
    exam_points = []
    exercises = []
    
    while True:
        user_input = input(f"Exam points and exercises completed: ")
        if user_input == "":
            break
        
        seperator_index = user_input.find(" ")
        exam_points.append(int(user_input[0:seperator_index]))
        exercises.append(int(user_input[seperator_index+1:]))
    
    print_statistics(exam_points, exercises)


def print_statistics(exam_points: list, exercises: list):
    exercise_points = determine_exercise_points(exercises)
    total_points = calculate_total_points(exam_points, exercise_points)
    
    grades = determine_grades(total_points)

    print("Statistics:")
    points_avg = calculate_points_avg(total_points)
    print(f"Points average: {points_avg}")

    pass_percentage = calculate_pass_percentage(grades)
    print(f"Pass percentage: {pass_percentage}")

    print("Grade distribution:")
    display_grade_distribution(grades)

def determine_exercise_points(exercises:list):
    exercise_points = []
    
    for i in exercises:
        exercise_point = 0

        if i == 100:
            exercise_point = 10
        elif i >= 90 :
            exercise_point = 9
        elif i >= 80 :
            exercise_point = 8
        elif i >= 70 :
            exercise_point = 7
        elif i >= 60 :
            exercise_point = 6
        elif i >= 50 :
            exercise_point = 5
        elif i >= 40 :
            exercise_point = 4
        elif i >= 30 :
            exercise_point = 3
        elif i >= 20 :
            exercise_point = 2
        elif i >= 10 :
            exercise_point = 1
        else:
            exercise_point = 0
        
        exercise_points.append(exercise_point)

    return exercise_points

def calculate_total_points(exam_points:list, exercise_points:list):
    total_points = []

    for i in range(0, len(exam_points)):
        total_points.append(exam_points[i] + exercise_points[i])
    
    return total_points

def determine_grades(total_points:list):
    grades = []

    for i in total_points:
        if i>=0 and i<=14:
            grade = 0
        elif i>=15 and i<=17:
            grade = 1
        elif i>=18 and i<=20:
            grade = 2
        elif i>=21 and i<=23:
            grade = 3
        elif i>=24 and i<=27:
            grade = 4
        elif i>=28 and i<=30:
            grade = 5

        grades.append(grade)
    
    return grades

def calculate_points_avg(total_points:list):
    sum = 0

    for i in total_points:
        sum += i

    return sum/len(total_points)

def calculate_pass_percentage(grades:list):
    pass_count = 0
    
    for i in grades:
        if i > 0:
            pass_count += 1

    return pass_count*100/len(grades)

def display_grade_distribution(grades:list):
    grades_distribution = []
    
    for i in range(5, -1, -1):
        distribution = ""
        for j in grades:
            if j == i:
                distribution += "*"
        print(f"{i}: {distribution}")

if __name__ == "__main__":
    main()