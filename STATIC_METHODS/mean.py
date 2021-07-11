from SOURCE.Calculator import addition
from SOURCE.Calculator import division

def mean(data):
    try:
        array_length = len(data)
        sum = 0
        for value in data:
            sum = addition(sum, value)
        return round(division(array_length, sum), 4)
    except ZeroDivisionError:
        print("Error: Cannot Divide by Zero")

