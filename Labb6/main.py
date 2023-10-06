import timeit

class Song:
   
    def __init__(self, trackid, songid, artist_name, songtitle ):
        self.trackid = trackid
        self.songid = songid
        self.artist_name = artist_name
        self.songtitle = songtitle

    def __lt__(self, other):
        if self.artist_name < other.artist_name:
            return True
        else:
            return False
    
    def __str__(self):
       return self.songtitle


def linsok(obj_list, testartist):
    for song in obj_list:
        if song.artist_name == testartist:
            return True
    return False


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        # Check if the middle element is equal to the target
        if arr[mid] == target:
            return target  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return None  # Target not found in the array

def sortera_artist(obj_list):
    artists = []
    for obj in obj_list:
        artists.append(obj.artist_name)
    return artists.sort()

def hash_search(dict, key):
    resultat = dict[key]


def main():

    obj_list = []

    with open("Labb6/unique_tracks.txt","r", encoding="utf-8") as track_file:
        for line in track_file:
            words = line.split("<SEP>")
            song_object = Song(words[0], words[1], words[2], words[3].strip("\n"))
            obj_list.append(song_object)

        """
        Linjärsökning: 
            n = 250 000, 14.041s
            n = 500 000, 0.8455s
            n = 1 000 000, 0.1537s

        men okej vi söker ju faktistk efter ett namn som kan uppstå fler ggr vilket kan påverka söktiden

        binärsökning: 
            n = 250 000, 0.0032
            n = 500 000, 0.8455s
            n = 1 000 000, 0.1537s
        """
        #linjärsökning - oserterad lista
        """
        #listan = obj_list
        #n = len(listan)
        #print("Antal element =", n)

        #sista = obj_list[n-1]
        #test = sista.artist_name
        
        
        # linjtid = timeit.timeit(stmt = lambda: linsok(obj_list, test), number = 10000) #9.2149
        # print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
    
        """
       # binary search
        """
        artists = []
        for obj in obj_list:
            artists.append(obj.artist_name)
        artists.sort()

        n = 250000
        artist_lst = artists[0:n]
        sista = artist_lst[n-1]
        print("Antal Element =", n)
        linjtid = timeit.timeit(stmt = lambda: binary_search(artist_lst, sista), number = 10000) #9.2149
        print("Binärsökningen tog", round(linjtid, 4) , "sekunder")
        """

        #hashning
        song_dict = {}

        for obj in obj_list:
            song_dict[obj.songtitle] = obj.trackid
        
        n_dict = 10000
        shortned_dict = song_dict[0:n_dict]

        print("Antal Element =", n_dict)
        linjtid = timeit.timeit(stmt = lambda: binary_search(shortned_dict, sista), number = 10000) #9.2149
        print("Binärsökningen tog", round(linjtid, 4) , "sekunder")

main()


    