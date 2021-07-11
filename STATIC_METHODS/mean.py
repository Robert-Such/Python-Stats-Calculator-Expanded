from SOURCE.Calculator import addition
from SOURCE.Calculator import division

def mean(data):
    try:
        num_values = len(data)
        sum = 0
        for num in data:
            sum = addition(sum, num)
        return round(division(num_values, sum), 4)
    except ZeroDivisionError:
        print("Error: Cannot Divide by Zero")

