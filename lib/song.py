from . import CURSOR

class Song:
    count = 0  # Initialize the count attribute to zero
    genres = set()  # Initialize the genres attribute as an empty set
    artists = set()  # Initialize the artists attribute as an empty set
    genre_count = {}  # Initialize the genre_count attribute as an empty dictionary
    artist_count = {}  # Initialize the artist_count attribute as an empty dictionary

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1  # Increment the count when a new Song object is created
        Song.genres.add(genre)  # Add the genre to the set of genres
        Song.artists.add(artist)  # Add the artist to the set of artists

        # Increment the genre count or initialize it if the genre is new
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Increment the artist count or initialize it if the artist is new
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

        
    @classmethod
    def create(cls, name, album):
        pass
        song = Song(name, album)
        song.save()
        return song
    
    @classmethod
    def create_table(self):
        pass
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        
        CURSOR.execute(sql)

    def save(self):
        pass
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        
        CURSOR.execute(sql, (self.name, self.album))
        
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]