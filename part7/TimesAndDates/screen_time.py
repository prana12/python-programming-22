from datetime import datetime, timedelta

def record_screen_time():
    filename = input("Filename: ")
    print(filename)

    # 24.6.2020
    starting_date_str = input("Starting date: ")
    starting_date = datetime.strptime(starting_date_str, "%d.%m.%Y")
    days = int(input("How many days: "))
    
    screen_times = {}
    count = 0
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    while count < days:
        key = starting_date.strftime("%d.%m.%Y")
        value = input(f"Screen time {key}: ")
        screen_times[key] = value
        count += 1
        starting_date = starting_date + timedelta(days=1)
    
    result = prepare_data(screen_times)
    write_data(result, filename)

def prepare_data(screen_times: dict):
    output = ""

    first_date = list(screen_times.keys())[0]
    last_date = list(screen_times.keys())[-1]
    total_mins = 0
    avg_mins = 0.0

    daily_screen_times = ""
    for key, values in screen_times.items():
        minutes = values.split(" ")        
        daily_screen_times += f"{key}: {'/'.join(minutes)}"

        for item in minutes:
            total_mins += int(item)
        daily_screen_times += "\n"

    avg_mins = total_mins/len(screen_times)

    output += f"Time period: {first_date}-{last_date}\n"
    output += f"Total minutes: {total_mins}\n"
    output += f"Average minutes: {avg_mins}\n"
    output += daily_screen_times

    return output

def write_data(output: str, filename: str):
    with open(filename, "w") as my_file:
        my_file.write(output)

if __name__ == "__main__":
    record_screen_time()