from hashtable import Hashtable
import csv


def main():
    kdrama_dict = {}
    with open('Labb7/kdrama.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            kdrama_dict[row[0]] = row[1]
           
    tabell = Hashtable(len(kdrama_dict)*2)
    for title, data in kdrama_dict.items():
        tabell.store(title, data)
    
    print(f"{len(kdrama_dict)} element")
    print(f"{tabell.collisions} krockar")
    

main()