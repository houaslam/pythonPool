import math


def NULL_not_found(object: any) -> int:
    nullValue = None
    if object is None:
        nullValue =  "Nothing"
    elif type(object) is float and math.isnan(object):
        nullValue =  "Cheese"
    elif type(object) is int and not object:
        nullValue =  "Zero"
    elif type(object) is str and not object:
        nullValue =  "Empty"
    elif type(object) is bool and not object:
        nullValue =  "Fake"
    else:
        print("Type not Found")
        return 1
    print(f"{nullValue} : {object} {type(object)}")
    return 0