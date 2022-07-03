import urllib.request
import certifi # add this library to your import section
import json

def retrieve_course(coursename: str):
    result = {}

    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{coursename}/stats"
    # add a second argument to the function call
    my_request = urllib.request.urlopen(address, cafile=certifi.where())

    course = json.loads(my_request.read())
    
    students_total = 0
    hours_total = 0
    exercise_total = 0
    
    for key, value in course.items():
        #print(key, value)
        students_total += value["students"]
        hours_total += value["hour_total"]
        exercise_total += value["exercise_total"]
    
    result['weeks'] = len(course)
    result['students'] = students_total
    result['hours'] = hours_total
    result['hours_average'] = hours_total//students_total
    result['exercises'] = exercise_total
    result['exercises_average'] = exercise_total//students_total
 
    return result

if __name__ == "__main__":
    output = retrieve_course("docker2019")
    print(output)