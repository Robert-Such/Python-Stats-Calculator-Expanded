from STATIC_METHODS.standard_deviation import standard_deviation
from STATIC_METHODS.squaring import squaring



def variance(data):

    CalculatedStandardDeviation = standard_deviation(data)

    Variance = squaring(CalculatedStandardDeviation)

    return round(Variance, 4)