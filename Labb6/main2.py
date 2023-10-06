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

def linsok(obj_list, testartist): #goes through entire list until you find the first obejct with correct artistname
    for song in obj_list:
        if song.artist_name == testartist:
            return True
    return False

#Taken from CHatGPT
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

def hash_search(dict, key):
    result = dict[key]

def sortera_artist(obj_list):
    artists = []
    for obj in obj_list:
        artists.append(obj.songid)
    return artists

def readfile():
    obj_lst = []
    with open("Labb6/unique_tracks.txt","r", encoding="utf-8") as track_file:
        for line in track_file:
            words = line.split("<SEP>")
            song_object = Song(words[0], words[1], words[2], words[3].strip("\n"))
            obj_lst.append(song_object)

    return obj_lst


#time complexity of O(n log n) in average in worst case O(n^2)
#taken from lecture 8
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista) 

def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v

#time complexity O(n^2)
def insattningssortera(data):
    n = len(data)
    for i in range(1, n):
        varde = data[i]
        plats = i
        while plats > 0 and data[plats-1] > varde:
            data[plats] = data[plats-1]
            plats = plats - 1
        data[plats] = varde

def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]


def main():
    obj_lst= readfile()
    n = 1000000
    print("Antal Element =", n)
    obj_lst = obj_lst[0:n]

    last = obj_lst[n-1]
    testkey = last.artist_name

    #linjtid = timeit.timeit(stmt = lambda: linsok(obj_lst, testkey), number = 10000) #9.2149
    #print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

    artist_lst = sortera_artist(obj_lst)
    artist_lst.sort()
    cut_artist_lst = artist_lst[0:n]
    testkey_bin = cut_artist_lst[n-1]
    bintid = timeit.timeit(stmt = lambda: binary_search(cut_artist_lst, testkey_bin), number = 10000) #9.2149
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")

    
    # obj_dict = {}

    # for count, obj in enumerate(obj_lst): #adds the objects in a dictonary with certain values key
    #     obj_dict[obj.artist_name] = obj.songid
    #     if count == n:
    #         break
    
    # hashtid = timeit.timeit(stmt = lambda: hash_search(obj_dict, testkey), number = 10000) #9.2149
    # print("Hasning tog", round(hashtid, 4) , "sekunder")


def sorterting_main():
    obj_lst = readfile()
    n = 100000
    print("Antal Element =", n)
    obj_lst = obj_lst[0:n]

    #sorttid = timeit.timeit(stmt= lambda: quicksort(obj_lst), number = 1) #0.002
    #print("Det tog", round(sorttid,4), "sekunde att sortera med quicksort")
   
    sorttid2 = timeit.timeit(stmt= lambda: insattningssortera(obj_lst), number = 1)
    print("Det tog", round(sorttid2,4), "sekunde att sortera med insättningssortering") #0.0428

    #sorttid3 = timeit.timeit(stmt= lambda: urvalssortera(obj_lst), number = 1)
    #print("Det tog", round(sorttid3,4), "sekunde att sortera med urvalssortering")
    
main()
#sorterting_main()

"""
Sökning
Linjärsökning har tidskomplexitet O(n). Vid sökning efter track_id (som är unika för varje objekt, inga dubletter) för n=1000, n=10 000 och n=100 000 fås resultaten 0.2s, 2.0s och 37s respektive. Detta motsvarar en ökning med ungefär en faktor 10 i tidsåtgång, för samma ökning av n.
Binärsökning har tidskomplexitet O(log n), 0.0208, 0.0219, 0.0229. En liten ökning vid växande n, men ungefär samma tid. Binärsökning halverar listan som söks genom varje iteration, ju längre lista desto fler iterationer men det är fortfarande en väldigt snabb sökmetod och eftersom tidskomplexiteten är logaritmisk så verkar den lilla ökningen i tid rimlig. 
hashsök - O(1), genom dictionary har vi lagt in saker på en specifik plats och därmed, när vi söker efter det vet vi exakt var den är. Därför tar det lika lång tid oberoende av antal element. 

Sortering
Långsam (insättning) - Worst case är O(n2). Om listan är sorterad i fallande ordning får vi worst case, eftersom varje element måste jämföras och byta plats med samtliga föregående element. Våra mätningar hamnar nära O(n2), med 0.036s, 3.93s och 554s för n=1000, n=10 000 och n=100 000 respektive. Om n ökar med faktor 10 så ökar tidsåtgången med ungefär en faktor 102.
Snabb (quick sort) - O(n log n) Genom matematiska beräkningar märkte vi att tiderna vi fick stämde överens med tidskomplexiteten. 

"""