import csv

class Drama:
    def __init__(self, drama_name, rating, actors, viewship_rate, genre, director, writer, year, no_episodes, network):
        self.drama_name = drama_name
        self.rating = rating
        self.actors = actors
        self.viewship_rate = viewship_rate
        self.genre = genre
        self.director = director
        self.writer = writer
        self.network = network
        self.year = year
        self.no_episodes = no_episodes
        self.network = network

    def __str__(self):
        return f"{self.drama_name} ({self.year})"
    
    def __lt__(self, other):
        #returns a boolean value based on the condition
        #writes true & false
        return self.rating < other.rating
    
    def get_genre(self):
        return f"Genren är {self.genre}"
    
    def get_writer_director(self):
        return f"Skriven av {self.clean_list(self.writer)} och regisserad av {self.clean_list(self.director)}"
    
    def clean_list(self, name_list):
        string = ""
        for index, person in enumerate(name_list):
            if index != 0:
                string += ", " + person
            else:
                string += person
        return string
    
obj1 = Drama("Suits", 8.4, ["Garbiel Macht", "Patrick J. Adam", "Gina Torres"], 17.6 , "drama", ["Aaron Korsh"],["Aaron Korsh"], 2011, 134, "USA Network")
obj2 = Drama("Avatar: the last airbender", 9.3, ["Aang", "Katara", "Sokka", "Momo"], 20.5 , "Adventure", ["Michale Dante DiMartino", "Byran Konietzko"], ["Michale Dante DiMatino", "Byran Konietzko"], 2005, 62, "Nickelodeon")

print(obj1)
print(obj1 < obj2)
print(obj2.get_genre())
print(obj2.get_writer_director())   

def read_file():
    objects = []
    with open('kdrama.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) #hoppar över första raden
        for row in csvreader:
            objects.append(Drama(row[0], row[1],row[2],row[3], row[4], row[5], row[6],row[7],row[8],row[9]))
    return objects 
            


dramas_list = read_file() #lista på alla object
print(dramas_list[0].get_genre())
    
def get_highly_rated_dramas(dramas_list):
    
    rating_input = float(input("Välj rating att söka efter (alla serier med samma eller högre rating kommer visaa: "))
    highly_rated = []
    for obj in dramas_list:
        if float(obj.rating) >= rating_input:
            highly_rated.append(str(obj))
    return highly_rated

for line in get_highly_rated_dramas(dramas_list):
    print("")
    print(line)

        