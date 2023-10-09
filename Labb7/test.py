import csv

class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, key, value):
        self.dict[key] = value
    
    def __getitem__(self, key):
        return self.dict[key]
    
    def __contains__(self, key):
        if key in self.dict:
            return True
        else:
            return False


"""
kdrama_dict = DictHash()
def read_file():
    with open('Labb7/kdrama.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            kdrama_dict.store(row[0], row[1])

read_file()
print(kdrama_dict["Legend of the Blue Sea"])
print("hello" in kdrama_dict)
"""




    