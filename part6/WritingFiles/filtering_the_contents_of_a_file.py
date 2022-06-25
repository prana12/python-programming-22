from array import array


def filter_solutions():
    solutions = read_entries()
    filter_entries(solutions)

def read_entries():
    solutions = []

    with open("solutions.csv") as new_file:
        for line in new_file:
            #line = line.replace("\n", "")
            solutions.append(line)
            
    return solutions

def filter_entries(solutions: array):
    for solution in solutions:
        parts = solution.split(";")
        
        n1 = int(parts[1][0])
        n2 = int(parts[1][2])
        operation = parts[1][1]
        result = int(parts[2])

        if(check_problem(n1, n2, operation, result)):
            write_entries(solution, "correct.csv")
        else:
            write_entries(solution, "incorrect.csv")

def check_problem(n1:int, n2:int, operation: str, result: int):
    if operation == "+":
        return n1+n2 == result
    elif operation == "-":
        return n1-n2 == result

def write_entries(solution:str, filename: str):
    with open(filename, "a") as my_file:
        my_file.write(solution)
    

if __name__ == "__main__":
    filter_solutions()
    