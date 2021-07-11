from SOURCE.Calculator import addition
from SOURCE.Calculator import subtraction
from SOURCE.Calculator import division


def median(data):
    array_length = len(data)
    data.sort(key=int)

    if array_length % 2 == 0:
        median1 = data[array_length // 2]
        median2 = data[int(subtraction(1, array_length // 2))]
        median = division(2, addition(median1, median2))
    else:
        median = data[array_length // 2]
    return median
