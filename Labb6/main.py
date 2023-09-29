class Song():
   
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

obj_list = []

with open("Labb6/unique_eighth.txt","r", encoding="utf-8") as track_file:
    for line in track_file:
        words = line.split("<SEP>")
        song_object = Song(words[0], words[1], words[2], words[3].strip("\n"))
        obj_list.append(song_object)


print(obj_list[1].__lt__(obj_list[0]))