import pandas as pd
from os import remove, path
import csv
from util import Util

class Convert:
    from_dir = None
    output_dir = None
    name_input = None
    name_output = None
    
    
    def __init__(self, base_dir, output_dir, name_input, name_output):
        self.from_dir = base_dir
        self.output_dir = output_dir
        self.name_input = name_input
        self.name_output = name_output


    def to_csv(self, sheet='Sheet1', dtype=str):
        data_xlsx = pd.read_excel(path.join(self.from_dir, self.name_input), sheet, dtype=dtype, index_col=0)
        data_xlsx.to_csv(path.join(self.output_dir, self.name_output),sep=';')

        self.remove_file()

    def to_json(self):
        rows = []
        with open(path.join(self.from_dir, self.name_input), 'r') as csv_file:
            reader = csv.reader(csv_file)
            header = ''
            c = 0
            for row in reader:
                if c == 0:
                    header = [Util.scape_string(item) for item in row]
                else:
                    json = {}
                    for i in range(len(header)):
                        json[header[i]] = row[i]
                    rows.append(json)
                c += 1
        return {'data':rows}

    

    def remove_file(self):
        remove(path.join(self.from_dir, self.name_input))
