from datetime import datetime, timedelta

def check_age():
    millennium_eve = datetime(1999, 12, 31)

    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    dob = datetime(year, month, day)
    
    difference = millennium_eve - dob
    if difference.days >= 0:
        print("You were", difference.days, "days old on the eve of the new millennium.")
    else:
        print("You weren't born yet on the eve of the new millennium.")

    #return result

if __name__ == "__main__":
    check_age()