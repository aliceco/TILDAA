import csv

class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, key, value):
        self.dict[key] = value
    
    def search(self, key):
        return self.dict[key]
        
    def __getitem__(self, key):
        if self.__contains__(key) is True:
            return self.search(key)
        else: 
            return f"{key} is not in file"
    
    def __contains__(self, key):
        if key in self.dict:
            return True
        else:
            return False


def read_file(kdrama_dict):
    with open('Labb7/kdrama.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            kdrama_dict.store(row[0], row[1])
    return kdrama_dict

def main():
    kdrama_dict = DictHash()
    dictt = read_file(kdrama_dict)
    print(dictt["heja"])
    print("hello" in kdrama_dict)

main()