def add_student(students: dict, name: str):
    if name not in students:
        students[name] = "no completed courses"

def add_course(students: dict, name: str, course: tuple):
    # course[0] and course[1]
    module, grade = course

    # Courses with grade 0 should be ignored
    if grade <= 0:
        return

    if students[name] == "no completed courses":
        courses = []
        courses.append(course)
        students[name] = courses
    else:
        for item in students[name]:
            # Ignore if the course is already in the database
            if item[0] == module:
                return
        students[name].append(course)

def print_student(students: list, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        grade_sum = 0
        print(f"{name}: \n {len(students[name])} completed courses:")
        for course in students[name]:
            module, grade = course
            grade_sum += grade
            print("  ", module, grade)
        print(f"\n average grade: {grade_sum/len(students[name])}")

def summary(students: list):
    print(f"students {len(students)}")
    most_courses_completed(students)
    best_average_grade(students)
    
def most_courses_completed(students: list):
    max_courses_completed = 0
    max_courses_completed_person = ""

    for key, value in students.items():
        if len(value) > max_courses_completed:
            max_courses_completed = len(value)
            max_courses_completed_person = key
    
    print(f"most courses completed {max_courses_completed} {max_courses_completed_person}")

def best_average_grade(students: list):
    best_average_grade = 0.0
    best_average_grade_person = ""

    for key, value in students.items():
        sum = 0

        for course in value:
            sum += course[1]
            
        avg = sum/len(course)
        if avg > best_average_grade:
            best_average_grade = avg
            best_average_grade_person = key

    print(f"best average grade {best_average_grade} {best_average_grade_person}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)