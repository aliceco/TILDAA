class song():
   
    def __init__(self, trackid, songid, artist_name, songtitle ):
        self.trackid = trackid
        self.songid = songid
        self.artist_name = artist_name
        self.songtitle = songtitle

    def __lt__(self, other):
        return self.artist_name < other.artist_name


with open("Labb6/unique_tracks.txt","r", encoding="utf-8") as track_file:
    for line in track_file:
        for information in range(0, 4):
            
        word = line.split("<SEP>")
        print(word)

