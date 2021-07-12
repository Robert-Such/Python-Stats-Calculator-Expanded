
from random import seed
from random import uniform


def randomdata(SeedRangeStart, SeedRangeEnd, Array_Length, MinValue, MaxValue):
	seed(uniform(SeedRangeStart, SeedRangeEnd))
	data = []
	for i in range(Array_Length):
		value = uniform(MinValue, MaxValue)
		data.append(value)

	data.extend((500, 500)) # Appending a repeating value to random set for testing mode function
	return(data)