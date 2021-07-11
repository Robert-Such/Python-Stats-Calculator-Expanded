from STATIC_METHODS.addition import addition
from STATIC_METHODS.subtraction import subtraction
from STATIC_METHODS.division import division
from STATIC_METHODS.squaring import squaring
from STATIC_METHODS.square_rooting import square_rooting
from STATIC_METHODS.mean import mean



def standard_deviation(data):

    total = 0
    array_length = len(data)
    CalculatedMean = mean(data)

    for value in data:
        total = addition(squaring(subtraction(CalculatedMean, value)), total)

    StandardDeviation = square_rooting(division(array_length, total))
    return round(StandardDeviation, 8)
