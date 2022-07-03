from datetime import datetime, timedelta

def cheaters():
    cheaters = []

    # READ start_times.csv
    start_times = read_start_times("start_times.csv")
    
    # READ submissions.csv
    submissions = read_submissions("submissions.csv")
    
    for name, start_time_value in start_times.items():
        if name in submissions:
            submissions_list = submissions[name]
            start_time = datetime.strptime(start_time_value, "%H:%M")
            
            for submission in submissions_list:
                submission_time = datetime.strptime(submission[2], "%H:%M")
                end_time = start_time + timedelta(hours=3)
                
                if submission_time > end_time:
                    cheaters.append(name)
                    break

    return cheaters

def read_start_times(filename: str):
    start_times = {}

    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            start_times[parts[0]] = parts[1]
    
    return start_times

def read_submissions(filename: str):
    submissions = {}

    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            submission_tuple = (parts[1], parts[2], parts[3]) # rest of the submission details

            if parts[0] in submissions:
                tasks = submissions[parts[0]]
                tasks.append(submission_tuple)
            else:
                tasks = []
                tasks.append(submission_tuple)
                
                submissions[parts[0]] = tasks

    return submissions

if __name__ == "__main__":
    output = cheaters()
    print(output)