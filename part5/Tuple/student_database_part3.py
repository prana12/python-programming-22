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

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")