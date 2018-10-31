class Song:
    """Class to represent a song
    
    Attributes:
        title (str): Title of the song
        artist (Artist): An artist object representing the song's creator
        duration (int): The durations of the song in seconds, may be zero
    """

    def __init__(self, title, artist, duration=0):
        # """ Song init method
        # Args:
        #     title (str): Initializes the "title" attribute
        #     artist (Artist): An Artist object representing the song's creator
        #     duration (Optional[int]: Initial vale for the "duration" attribute
        #         Will default to zero if not specified
        # """
        self.title = title
        self.artist = artist
        self.duration = duration

# help(Song.__init__)
print(Song.__doc__)
print(Song.__init__.__doc__)
# Below is dumb code and not a good idea but a good demonstration
Song.__init__.__doc__= """ Song init method
Args:
    title (str): Initializes the "title" attribute
    artist (Artist): An Artist object representing the song's creator
    duration (Optional[int]: Initial vale for the "duration" attribute
        Will default to zero if not specified
"""

help(Song)

================================================================================================

