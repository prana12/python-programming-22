from datetime import datetime

# The first half of the code is a valid, existing date in the format ddmmyy.
# The century marker is either + (1800s), - (1900s) or A (2000s).
# The control character is valid.

def is_it_valid(pic: str):
    #1 DOB
    dob = pic[:6]
    try :
        #print(int(dob[4:6]),int(dob[2:4]),int(dob[:2]))
        datetime(int(dob[4:6]),int(dob[2:4]),int(dob[:2])) #yymmdd
    except ValueError :
        #raise ValueError("Invalid DOB")
        print("error in dob")
        return False


    #2 Century Marker
    century = pic[6]
    invalid_century = century != "+" and century != "-" and century != "A"

    if invalid_century:
        #raise ValueError("Invalid Century Marker")
        print("error in century marker")
        return False


    #3 Control character
    valid_control_chars="0123456789ABCDEFHJKLMNPRSTUVWXY"
    nine_digit_number = int(pic[:6] + pic[7:10])
    control_char = valid_control_chars[nine_digit_number%31]
    
    if control_char != pic[10:11]:
        #raise ValueError("Invalid Character Control")
        print("error in character control")
        return False

    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))