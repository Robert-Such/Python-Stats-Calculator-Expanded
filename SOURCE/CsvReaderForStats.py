import csv
from collections import defaultdict


class CsvReaderForStats:

    def __init__(self, filepath):
        self.column = defaultdict(list)
        with open(filepath) as text_data:
            data = csv.DictReader(text_data, delimiter=',')
            for row in data:
                for (x, y) in row.items():
                    self.column[x].append(y)
        pass
