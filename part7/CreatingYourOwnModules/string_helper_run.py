#import string_helper
from string_helper import change_case, split_in_half, remove_special_characters

def test():

    my_string = "Well hello there!"
    #print(string_helper.change_case(my_string))
    print(change_case(my_string))

    #p1, p2 = string_helper.split_in_half(my_string)
    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    #m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)

if __name__ == "__main__":
    test()