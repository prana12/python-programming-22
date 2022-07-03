import urllib.request
import certifi # add this library to your import section
import json

def retrieve_all():
    result = []

    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    # add a second argument to the function call
    my_request = urllib.request.urlopen(address, cafile=certifi.where())

    courses = json.loads(my_request.read())
    for course in courses:
        if course["enabled"] == True:
            result.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))

    return result

if __name__ == "__main__":
    output = retrieve_all()
    print(output)