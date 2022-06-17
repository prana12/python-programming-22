def smallest(x:int, y:int, z:int):
    if x < y and x <z:
        return x
    elif y < z:
        return y
    else:
        return z

def greatest(x:int, y:int, z:int):
    if x > y and x >z:
        return x
    elif y > z:
        return y
    else:
        return z

def sum(x:int, y:int, z:int):
    return x+y+z

def create_tuple(x: int, y: int, z: int):
    smallest_number = smallest(x, y, z)
    greatest_number = greatest(x, y, z)
    sum_total = sum(x, y, z)

    my_tuple = (smallest_number, greatest_number, sum_total)
    return my_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))